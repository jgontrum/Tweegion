#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion

blackwords = ["data/stoppwords200.txt"]
tweets = ["data/geo-tweets/unbalanced_175k.json"]
geo = ["data/geo-tweets/balanced-39k.json"]
loops = [0,1,2,3,4,5,10,15,20]
guesses = [0.2]

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