#/usr/bin/ python
# -*- coding: utf8 -*-
import csv               # Lesen und Schreiben von CSV-Dateien
import sys
import os
import json
import codecs
from numpy import array  # Datenstruktur für Vektoren
import numpy
from happyfuntokenizing import Tokenizer
import geo
import Use

###########################################################
# Nutzereingabe:
# init_wv_file    CSV-Datei mit initialen Wortvektoren
# tweets_file     Datei mit Tweets (JSON-Objekte)
# stopwords_file  Textdatei mit Stoppwörtern
###########################################################
init_wv_file = "Words/Regionalwords.csv"
tweets_file = "./"
stopwords_file = "Wordcount/stpwds_no_happytok.txt"
geo_tagged_tweets = "first_geo_tweets.txt"

# CSV einlesen und als Dictionary von Wortvektoren ausgeben
def csv_to_vectors(filename):
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

def geodict_to_vectors(geodict):
    wv = {}
    for tweet_id in geodict:
        tweet,region = geodict[tweet_id]
        for token in tweet:
            if token in wv:
                wv[token] += get_region_vector(region)
            else:
                wv[token] = get_region_vector(region)
    for word in wv:
        wv[word] = normalize(wv[word])

    return wv


def get_region_vector(region):
    if region == 0:
        return array([1.0,0.0,0.0,0.0,0.0,0.0,0.0])
    if region == 1:
        return array([0.0,1.0,0.0,0.0,0.0,0.0,0.0])
    if region == 2:
        return array([0.0,0.0,1.0,0.0,0.0,0.0,0.0])
    if region == 3:
        return array([0.0,0.0,0.0,1.0,0.0,0.0,0.0])
    if region == 4:
        return array([0.0,0.0,0.0,0.0,1.0,0.0,0.0])
    if region == 5:
        return array([0.0,0.0,0.0,0.0,0.0,1.0,0.0])
    if region == 6:
        return array([0.0,0.0,0.0,0.0,0.0,0.0,1.0])



# Tweets einlesen und als Dictionary ID -> Text ausgeben
def jsons_to_dict(path, stopwords):
    id_to_tok = dict()
    tok = Tokenizer(preserve_case=False)
    for tweetfile in [folder for folder in os.listdir(path) if folder.startswith('first10000') == True ]:
        tweetfile = os.path.join(path, tweetfile)
        with codecs.open(tweetfile, 'r', "utf-8") as json_file:
            for line in json_file:
                try:
                    tweet = json.loads(line, 'latin1')['text']
                    tweet_id = json.loads(line, 'latin1')['id']
                    tokenized_tweet = tok.tokenize(tweet)
                    # Stopworte entfernen
                    id_to_tok[tweet_id] = [token for token in tokenized_tweet if token not in stopwords]
                except:
                    None
    return id_to_tok

# Raw Text einlesen und als Liste ausgeben
def textfile_to_list(filename):
    textfile = open(filename,'r')
    return textfile.readlines()

# Hauptalgorithmus: aus gegebener Generation von Wortvektoren die nächste berechnen
def calc_next_generation(wvm, tweets):
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

    for word in wvn:
        wvn[word] = normalize(wvn[word])

    return wvn

# Herunterrechnen eines Vektors, so dass er Summe 1 hat
def normalize(vector):
    ## Werden uns die Rundungsfehler auffressen? ##
    if vector.sum() > 0:
        return vector/vector.sum()
    return array([0.0,0.0,0.0,0.0,0.0,0.0,0.0])

def geo_to_dict(filename):
    id_to_geotok = dict()
    tok = Tokenizer(preserve_case=False)
    geo_functions = geo.GeoFunctions()
    with codecs.open(filename, 'r', "utf-8") as json_file:
        for line in json_file:
            try:
                json_data = json.loads(line, 'latin1')
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
            except:
                None
    return id_to_geotok


def average_distribution(wv):
    return sum(wv.values())/len(wv)

# Tweets und Stoppwörter einlesen
stopwords = textfile_to_list(stopwords_file)
tweets = jsons_to_dict(tweets_file,stopwords) 
# Wortvektoren der 0. Generation einlesen
#wv0 = csv_to_vectors(init_wv_file)
wv0 = geodict_to_vectors(geo_to_dict(geo_tagged_tweets))

# Erster Durchlauf, um 1. Generation dann mit 0. Generation vergleichen zu können
wv1 = calc_next_generation(wv0, tweets)
# Schleife - vergleiche stets die gerade berechnete Generation mit der vorigen
# Wenn sie größer ist, hat sie mehr Einträge, es sind also neue Wörter hinzugekommen
c = 0
#while len(wv1) > len(wv0):
while c < 5: 

    c += 1
    # In diesem Fall wird die alte Generation vergessen, ihren Platz nimmt die
    # gerade berechnete ein
    wv0 = wv1
    # Aus ihr wird die nächste Generation berechnet
    wv1 = calc_next_generation(wv0, tweets)
else:
    # Ist die gerade berechnete Generation nicht größer, enthielt die vorige bereits
    # alle Wörter des Trainingskorpus. Es wird also die vorige abgespeichert
    # for key,value in wv0.iteritems():
    #     print key
    #     print value
    # av = average_distribution(wv0)
    # for key,value in wv0.iteritems():
    #     deviation = value - av
    #     if numpy.amax(deviation) > 0.05 or numpy.amin(deviation) < -0.05:
    #         print key
    #         print deviation
    # print "Durchläufe"
    # print c
    print "Normalverteilung:"
    print average_distribution(wv0)

    tweet = "Schalke wird Meister, weil...... Meine unschlagbare Meisterschaftsargumentation gibbet in mein Block: http://www.ottos-revier.de/?p=1225  #ligaprognose" 
    Use.print_results(Use.classify_tweet(tweet,wv0))
    print Use.classify_tweet(tweet,wv0)

