#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot
from include.tweegion_log import Tweegion as TweegionLog

blackwords = ["data/stoppwords200.txt"]
tweets = ["data/geo-tweets/unbalanced_175k.json"]
geo = ["data/geo-tweets/balanced-21k.json", "data/geo-tweets/balanced-39k.json", "data/geo-tweets/balanced-61k.json", "data/geo-tweets/unbalanced_175k.json"]
loops = [0]

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
