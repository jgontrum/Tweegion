#/usr/bin/ python
# -*- coding: utf8 -*-
import csv               # Lesen und Schreiben von CSV-Dateien
from numpy import array  # Datenstruktur für Vektoren

###########################################################
# Nutzereingabe:
# init_wv_file    CSV-Datei mit initialen Wortvektoren
# tweets_file     Datei mit Tweets (JSON-Objekte)
# stopwords_file  Textdatei mit Stoppwörtern
###########################################################

# CSV einlesen und als Dictionary von Wortvektoren ausgeben
def csv_to_vectors(filename):
    wv = {}
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=';')
        for stringlist in csvreader:
            word = stringlist[0]
            floatlist = [float(x) for x in stringlist[1:]]
            wv[word] = array(floatlist)
    return wv

# Tweets einlesen und als Dictionary ID -> Text ausgeben
def jsons_to_dict(filename):
    ## ... ##

# Raw Text einlesen und als Liste ausgeben
def textfile_to_list(filename):
    textfile = open(filename,'r')
    return textfile.readlines()

# Hauptalgorithmus: aus gegebener Generation von Wortvektoren die nächste berechnen
def calc_next_generation(wvm):
    wvn = {}
    tv = {}
    
    for id, text in tweets.iteritems():
        
        tv[id] = array([0,0,0,0,0,0,0])
        for token in text:
            if not token in stopwords:
                tv[id] += wvm[token]
                
        for token in text:
            if not token in stopwords:
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
    return vector/vector.sum()


# Tweets und Stoppwörter einlesen
tweets = jsons_to_dict(tweets_file)
stopwords = textfile_to_list(stopwords_file)
# Wortvektoren der 0. Generation einlesen
wv0 = csv_to_vectors(init_wv_file)
# Erster Durchlauf, um 1. Generation dann mit 0. Generation vergleichen zu können
wv1 = calc_next_generation(wv0)
# Schleife - vergleiche stets die gerade berechnete Generation mit der vorigen
# Wenn sie größer ist, hat sie mehr Einträge, es sind also neue Wörter hinzugekommen
while wv1 > wv0:
    # In diesem Fall wird die alte Generation vergessen, ihren Platz nimmt die
    # gerade berechnete ein
    wv0 = wv1
    # Aus ihr wird die nächste Generation berechnet
    wv1 = calc_next_generation(wv0)
else:
    # Ist die gerade berechnete Generation nicht größer, enthielt die vorige bereits
    # alle Wörter des Trainingskorpus. Es wird also die vorige abgespeichert
    save(wv0)

