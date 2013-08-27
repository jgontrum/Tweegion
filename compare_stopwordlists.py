#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion

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