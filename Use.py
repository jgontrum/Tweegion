#/usr/bin/ python
# -*- coding: utf8 -*-
import csv               # Lesen und Schreiben von CSV-Dateien
from numpy import array  # Datenstruktur für Vektoren

# Dictionary Vektorstelle -> Regionenname
region = {0 : "Ostdeutschland",
          1 : "Norddeutschland",
          2 : "Westdeutschland",
          3 : "Südwestdeutschland",
          4 : "Bayern",
          5 : "Schweiz",
          6 : "Österreich"}

# Vektor für einen Tweet auf Grundlage von Wortvektoren berechnen
def classify_tweet(tweet_text,word_vectors):
    tweet_vector = array([0,0,0,0,0,0,0])
    for token in tweet_text:
        if token in word_vectors:
            tweet_vector += word_vectors[token]
    return tweet_vector

# Ergebnis der Klassifikation ausgeben
def print_results(tweet_vector):
    # Größten Wert des Vektors finden
    maxval = tweet_vector.max()
    if maxval == 0.0:
        # Nullvektor: keine regionalen Wörter gefunden
        print "Keine regionalen Wörter gefunden."
        return
    # Stelle des größten Wertes finden
    maxarg = []
    maxarg[0] = tweet_vector.argmax()
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
            maxarg[n+1] = rest.argmax() + n+1
        else:
            # Er ist kleiner: keine weiteren Treffer, Schleife beenden
            break
        n += 1
    # Ergebnisse ausgeben
    if len(maxarg) == 1:
        # Größter Wert in genau einer Region
        print "Der Tweet scheint aus der Region {0} zu stammen.".format(region[maxarg[0]])
        return
    else:
        # Größter Wert in mehreren Regionen
        results = ', '.join([region[m] for m in maxarg])
        print "Der Tweet scheint aus einer der Regionen {0} zu stammen.".format(results)
        return

