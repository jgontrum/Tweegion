#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot

blackwords = ["data/stoppwords200.txt", "data/stoppwords500.txt", "data/stoppwords750.txt", "data/stoppwords1000.txt"]
tweets = ["data/geo-tweets/balanced-21k.json", "data/geo-tweets/balanced-39k.json", "data/geo-tweets/balanced-61k.json", "data/geo-tweets/unbalanced-175k.json"]
geo = ["data/geo-tweets/balanced-21k.json", "data/geo-tweets/balanced-39k.json", "data/geo-tweets/balanced-61k.json", "data/geo-tweets/unbalanced-175k.json"]
loops = [0,1,3,5,10]

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
				tweegion = TweegionRoot("geo",
 					tweet,
 					blackword,
 					loop,
 					geot,
 					"")
				tweegion.evaluate_accuracy("data/geo-tweets/gold.json")