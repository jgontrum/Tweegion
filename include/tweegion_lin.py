#/usr/bin/ python
# -*- coding: utf8 -*-

import csv               # Lesen und Schreiben von CSV-Dateien
import sys
import json
import codecs
from numpy import array  # Datenstruktur für Vektoren
import numpy             # Weitere Funktionen für die Verrechnung von Vektoren
from happyfuntokenizing import Tokenizer    # Potts Tokenizer
import geo_wrapper as geo# Klassifizierung von Geo-Tweets
import matplotlib.pyplot as plt 
from pylab import arange,sqrt
import pylab

class Tweegion(object):
    __average_distribution = ()
    __wv = dict()
    __sim_threshold = 0
    # Dictionary Vektorstelle -> Regionenname
    __region = {0 : "Ostdeutschland",
              1 : "Norddeutschland",
              2 : "Westdeutschland",
              3 : "Südwestdeutschland",
              4 : "Bayern",
              5 : "Schweiz",
              6 : "Österreich"}

    __verbose = {   "Mode" : None, 
                    "Loops" : None, 
                    "Number of Tweets" : None, 
                    "Number of blackwords" : None,
                    "Number of regional words" : None,
                    "Number of Geo-Tweets" : None,
                    "Blacklist path" : None,
                    "Tweet path" : None,
                    "Regio path" : None,
                    "Geo path" : None,
                    "Calculation method" : None,
                    "Similarity" : None
                }

    # Arguments:
    #   * mode = "geo" | "regio" 
    #       Toggles the mode of Tweegion.
    #   * tweets = /path/to/json_tweet_objects (separeted by newline)
    #       Used in the loop for the calculation of all token
    #   * blackwords = /path/to/blackword_file (separated by newline)
    #       List of token, that will be ignored (e.g. the 100 token)
    #   * loops = int
    #       Numer of loops to calculate the distribution of the token
    #   * geo_tweets = /path/to/json_tweet_objects (separeted by newline)
    #       Used only in "geo"-mode. Tweet objects, that must contain a geo object!
    #   * regional_words = /path/to/csv_file (separated by semi-column)
    #       Used only in "regip"-mode. CSV file with regional words.
    #   * non_regional_tweets = <= 1 && >= 0
    #       Amount of all Tweets, that supose to have some regional token. 
    #       Used to calculate a similarity threshold 
    def __init__(self, mode, tweets, blackwords, loops, geo_tweets, regional_words, non_regional_tweets = 0.6):
        # Read blackwords
        blackword_list = self.__textfile_to_list(blackwords)
        # Parse and tokenize all tweets to get a dictionary (ID -> list_of_token)
        tweet_dict = self.__jsons_to_dict(tweets,blackword_list) 
        # Depending on the mode, create the first vector-list from geo-tagged tweets or read it from a CSV-file
        if mode == "geo":
            # geo_dict: Key: TweetID, Value: Tupel of a list of token for a tweet and the region index.
            geo_dict = self.__geo_to_dict(geo_tweets, blackword_list)
            # create the first wordvector depending an the previously created geo_dict
            wv0 = self.__geodict_to_vectors(geo_dict)
        elif mode == "regio":
            # in regio-mode we use a parsed CSV-file as first wordvector
            wv0 = self.__csv_to_vectors(regional_words)
        else:
            print "Please choose a valid mode: \"geo\" or \"regio\"."
            sys.exit(1)
        # print blackword_list
        # First  calculation based on the initial wordvector
        wv1 = self.__calc_next_generation(wv0, tweet_dict)
        # Entering the main-loop...
        counter = 0
        while counter < loops:
            counter += 1
            # the old wv1 is our new wv0!
            wv0 = wv1
            wv1 = self.__calc_next_generation(wv0, tweet_dict)
        self.__wv = wv1
        self.__calc_average_distribution()
        sim_list = self.__sorted_sim_list(tweet_dict, self.__wv, self.__average_distribution)
        self.__sim_threshold = sim_list[int(non_regional_tweets * len(sim_list))]
        self.__fill_verbose("Legacy", mode, loops, tweet_dict, blackword_list, regional_words, geo_tweets, blackwords, tweets, self.__sim_threshold)

    # Returns the region, from where a tweet was most likely sent. For more information, enable verbose mode
    def classify(self, tweet, human_readable=True, verbose=False):
        if not verbose:
            return self.__get_results(self.__classify_tweet(tweet), human_readable)
        else:
            pass

    # Arguments:
    #   * gold_tweet_file = /path/to/json_tweet_objects
    #       Must contain a geo field
    def evaluate_accuracy(self, gold_tweet_file):
        match = 0 #< Number tweets, where the actual region matches the calculated one
        mismatch = 0 #< not match
        lines =0
        geo_functions = geo.GeoFunctions()
        # Open the file and parse all json objects
        with codecs.open(gold_tweet_file, 'r', "utf-8") as json_file:
            for line in json_file:
                lines += 1
                json_data = json.loads(line, 'utf-8')
                tweet = json_data['text']
                coordinates = json_data['geo']['coordinates']
                region = geo_functions.get_region((float(coordinates[0]),float(coordinates[1])))
                if region != -1:
                    result = self.classify(tweet,False,False)
                    if result != -1:
                        if result == region: match += 1
                        else: mismatch += 1
        print ""
        print "Match: ", match
        print "Mismatch: ", mismatch
        print "Not regional: ", lines - (match + mismatch)
        print "Accuracy: ", float(match) / (match+mismatch)
        print "~~~~~~~~~~~~~~~~~~~~~"
        print "Variables:"
        for key, value in self.__verbose.iteritems():
            if value != None:
                print key, ":\t", value

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Internal functions:
    def __fill_verbose(self, method, mode, loops, tweets, blackwords, 
                        regio_path, geo_path, backword_path, tweet_path, sim):
        self.__verbose['Mode'] = mode
        self.__verbose['Loops'] = loops
        self.__verbose['Number of Tweets'] = len(tweets)
        self.__verbose['Number of blackwords'] = len(blackwords)
        self.__verbose['Blacklist path'] = backword_path
        self.__verbose['Tweet path'] = tweet_path
        self.__verbose['Calculation method'] = method
        self.__verbose['Similarity'] = sim
        if regio_path != "":
            self.__verbose['Regio path'] = regio_path
            i = 0
            with open(regio_path) as f:
                for i, l in enumerate(f):
                    pass
            self.__verbose['Number of regional words'] = i
        if geo_path != "":
            self.__verbose['Geo path'] = geo_path
            i = 0
            with open(geo_path) as f:
                for i, l in enumerate(f):
                    pass
            self.__verbose['Number of Geo-Tweets'] = i+1

    # Raw Text einlesen und als Liste ausgeben
    def __textfile_to_list(self, filename):
        return codecs.open(filename,'r',"utf-8").read().splitlines()
    
    # Tweets einlesen und als Dictionary ID -> Text ausgeben
    def __jsons_to_dict(self, tweet_file, stopwords):
        counter = 0
        id_to_tok = dict()
        tok = Tokenizer(preserve_case=False)
        with codecs.open(tweet_file, 'r', "utf-8") as json_file:
            for line in json_file:
                try:
                    tweet = json.loads(line, 'utf-8')['text']
                    tweet_id = json.loads(line, 'utf-8')['id']
                    tokenized_tweet = tok.tokenize(tweet)
                    # Stopworte entfernen
                    id_to_tok[tweet_id] = [token for token in tokenized_tweet if token not in stopwords]
                    counter += 1
                    # if counter % 1000 == 0:
                        # sys.stdout.write('+ ')
                except:
                    None
        return id_to_tok

    def __geo_to_dict(self, filename, stopwords):
        counter = 0
        id_to_geotok = dict()
        tok = Tokenizer(preserve_case=False)
        geo_functions = geo.GeoFunctions()
        with codecs.open(filename, 'r', "utf-8") as json_file:
            for line in json_file:
                try:
                    json_data = json.loads(line, 'utf-8')
                    tweet_id = json_data['id']
                    tweet = json_data['text']
                    coordinates = json_data['geo']['coordinates']
                    region = geo_functions.get_region((float(coordinates[0]),float(coordinates[1])))
                    # Stopworte entfernen
                    if region != -1:
                        tokenized_tweet = tok.tokenize(tweet)
                        id_to_geotok[tweet_id] = (
                            [token for token in tokenized_tweet if token not in stopwords],
                            region)
                    counter += 1
                    # if counter % 1000 == 0:
                        # sys.stdout.write('- ')
                except:
                    None
        return id_to_geotok

    def __geodict_to_vectors(self, geodict):
        wv = {}
        for tweet_id in geodict:
            tweet,region = geodict[tweet_id]
            for token in tweet:
                if token in wv:
                    wv[token] += self.__get_region_vector(region)
                else:
                    wv[token] = self.__get_region_vector(region)

        return wv

    # CSV einlesen und als Dictionary von Wortvektoren ausgeben
    def __csv_to_vectors(self, filename):
        wv = {}
        with codecs.open(filename,'r',"utf8") as csvfile:
            # Erste Zeile ignorieren
            csvfile.readline()
            for line in csvfile:
                stringlist = line.split(";")
                word = stringlist[0]
                floatlist = list()
                for x in stringlist[1:8]:
                    if x == "0.33":
                        floatlist.append(float(1/3.0))
                    elif x == "":
                        floatlist.append(0.0)
                    else:
                        floatlist.append(float(x))
                wv[word] = array(floatlist)
        return wv

    def __get_region_vector(self, region):
        vector = array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])
        vector[region] = 1.0
        return vector

    # Herunterrechnen eines Vektors, so dass er Summe 1 hat
    def __normalize(self, vector):
        ## Werden uns die Rundungsfehler auffressen? ##
        if vector.sum() > 0:
            return vector/vector.sum()
        return array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Herunterrechnen eines Vektors, so dass er Länge 1 hat
    def __normalize_len(self, vector):
        if vector.sum() > 0:
            return vector/numpy.linalg.norm(vector)
        return array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    # Hauptalgorithmus: aus gegebener Generation von Wortvektoren die nächste berechnen
    def __calc_next_generation(self, wvm, tweets):
        wvn = {}    # wvn = Dict von Wörtern auf Wort-Vektoren der n-ten Generation
        tv = {}     # tv = Dict von TweetIDs auf Tweet-Vektoren
        
        for id, text in tweets.iteritems():
            tv[id] = array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])
            for token in text:
                if token in wvm:
                    tv[id] += wvm[token]
            if tv[id].sum() > 0:
                for token in text:
                    if token in wvn:
                        wvn[token] += tv[id]
                    else:
                        wvn[token] = tv[id]

        return wvn

    # Vektor für einen Tweet auf Grundlage von Wortvektoren berechnen
    def __classify_tweet(self,tweet_text):
        tweet_vector = array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])
        tok = Tokenizer(preserve_case=False)
        for token in tok.tokenize(tweet_text):
            if token in self.__wv:
                tweet_vector += self.__wv[token]
        if self.__cosine_sim(tweet_vector, self.__average_distribution) > self.__sim_threshold:
            return None
        tweet_vector_normalized = self.__normalize_len(tweet_vector)
        tweet_vector_diff = tweet_vector_normalized - self.__average_distribution
        return tweet_vector_diff

    def __cosine_sim(self, q, d):
        # See Jurafsky & Martin: Speech and Language Processing, pp. 803: Information Retrieval - The Vector Space Model
        numerator = sum(q*d)
        denumerator = numpy.sqrt(sum(numpy.power(q,2))) * numpy.sqrt(sum(numpy.power(d,2)))
        if denumerator != 0:
            return numerator / denumerator
        return None

    def __get_raw_tv(self, tweet):
        tv = array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])
        for token in tweet:
            if token in self.__wv:
                tv += self.__wv[token]
        return tv

    def __sorted_sim_list(self, tweets, wv, average):
        sim_list = list()
        for tweet in tweets.values():
            tv = self.__get_raw_tv(tweet)
            cos = self.__cosine_sim(tv, average)
            if cos != None: # = Not a 0-Vector
                sim_list.append(cos)
        # fig_width_pt = 418.25  # Get this from LaTeX using \showthe\columnwidth
        # inches_per_pt = 1.0/72.27               # Convert pt to inches
        # golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
        # fig_width = fig_width_pt*inches_per_pt  # width in inches
        # fig_height =fig_width*golden_mean+1       # height in inches
        # fig_size = [fig_width,fig_height]
        # params = {'backend': 'ps',
        #     'axes.labelsize': 11,
        #     'text.fontsize': 11,
        #     'legend.fontsize': 11,
        #     'xtick.labelsize': 8,
        #     'ytick.labelsize': 8,
        #     'text.usetex': True,
        #     'figure.figsize': fig_size,
        #     'font.family' : 'serif'}
        # pylab.rcParams.update(params)
        # pylab.figure(1)
        # pylab.clf()
        # pylab.plot(sorted(sim_list)[::-1],label=r'$sim(\vec{d_x}, \vec{\bar{d}})$')
        # pylab.ylabel('cosine similarity')
        # pylab.xlabel(r'Tweet-vectors $\vec{d_x}$')
        # pylab.grid(True)
        # pylab.legend(loc=3)
        # pylab.savefig('doc/Hausarbeit/img/cos-verteilung.eps')
        return sorted(sim_list)


    def __calc_average_distribution(self):
        total_vector = sum(self.__wv.values())
        self.__average_distribution = self.__normalize_len(total_vector)

    # Ergebnis der Klassifikation ausgeben
    def __get_results(self, tweet_vector, human_readable=True):
        # Größten Wert des Vektors finden
        if tweet_vector == None:
            if human_readable:
                return "Der Tweet beinhaltet zu wenig relevante Wörter, um einer Region zugeordnet zu werden."
            else:
                return -1
        maxval = tweet_vector.max()
        if maxval == 0.0:
            # Nullvektor: keine regionalen Wörter gefunden
            if human_readable:
                return "Keine regionalen Wörter gefunden."
            else: return -1
        # Stelle des größten Wertes finden
        maxarg = []
        maxarg.append(tweet_vector.argmax())
        # Steht der größte Wert an mehreren Stellen, wird zunächst nur die erste gefunden
        # Daher den restlichen Vektor mit einer Schleife weiter durchsuchen
        n = 0
        # Solange der aktuelle Fund nicht am Ende des Vektors steht
        while maxarg[n] < 6:
            # Betrachte den Teil des Vektors dahinter
            rest = tweet_vector[maxarg[n]+1:]
            # Finde dort den größten Wert
            if rest.max() == maxval:
                # Er entspricht bisherigem größtem Wert: Stelle in Trefferliste speichern
                maxarg.append(rest.argmax() + n+1)
            else:
                # Er ist kleiner: keine weiteren Treffer, Schleife beenden
                break
            n += 1
        # Ergebnisse ausgeben
        if len(maxarg) == 1:
            # Größter Wert in genau einer Region
            if human_readable:
                return "Der Tweet scheint aus der Region {0} zu stammen.".format(self.__region[maxarg[0]])
            else: return maxarg[0]
        else:
            # Größter Wert in mehreren Regionen
            if human_readable:
                results = ', '.join([self.__region[m] for m in maxarg])
                return "Der Tweet scheint aus einer der Regionen {0} zu stammen.".format(results)
            else: return maxarg
            
if __name__ == "__main__":
   pass
