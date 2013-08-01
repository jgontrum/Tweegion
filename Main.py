#/usr/bin/ python
# -*- coding: utf8 -*-
from numpy import array  # Datenstruktur für Vektoren
import wv0               # Dictionary der initialen Wortvektoren {word : vector}
import tweets            # Dictionary von Tweets {id : text}
import stopwords         # Liste von Stoppwörtern

def calc_next_generation(wv0):
    wv1 = {}
    tv = {}
    
    for id, text in tweets.iteritems():
        
        tv[id] = array([0,0,0,0,0,0,0])
        for token in text:
            if not token in stopwords:
                tv[id] = tv[id] + wv0[token]
                
        for token in text:
            if not token in stopwords:
                # Initialisierung von wv1[token] fehlt!
                wv1[token] = wv1[token] + tv[id]
                
    for word in wv1:
        wv1[word] = normalize(wv1[word])

    return wv1

def normalize(vector):
    # Werden uns die Rundungsfehler auffressen?
    return vector/vector.sum()


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

