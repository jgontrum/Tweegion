#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion



# executes the tweegion-alogorithm for the geo-location-attempt and show results
# for different numbers of stopwords
# normalisation-method: normalized
# loops are fixed to 1

# please execute in command-line: nohup python compare_cos_sim.py > xxx.results &

blackwords = ["data/stoppwords200.txt","data/stoppwords500.txt","data/stoppwords750.txt","data/stoppwords1000.txt"]
tweets = ["data/geo-tweets/unbalanced_175k.json"]
geo = ["data/geo-tweets/balanced-39k.json"]
loops = [1]

for loop in loops:
	for blackword in blackwords:
		for tweet in tweets:
			for geot in geo:
				tweegion = Tweegion("geo",
 					tweet,
 					blackword,
 					loop,
 					geot,
 					"")
				tweegion.evaluate_accuracy("data/geo-tweets/gold.json")