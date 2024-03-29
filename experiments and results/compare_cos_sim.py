#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion


# executes the tweegion-alogorithm for the geo-location-attempt and show results
# for different cos_similarities
# stopwords are fixed to 200
# loops are fixed to 0

# please execute in command-line: nohup python compare_cos_sim.py > xxx.results &


blackwords = ["data/stoppwords200.txt"]
tweets = ["data/geo-tweets/unbalanced_175k.json"]
geo = ["data/geo-tweets/balanced-61k.json"]
loops = [0]
guesses = [0.9999999, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]

for guess in guesses:
	for loop in loops:
		for blackword in blackwords:
			for tweet in tweets:
				for geot in geo:
					tweegion = Tweegion("geo",
	 					tweet,
	 					blackword,
	 					loop,
	 					geot,
	 					"",
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
