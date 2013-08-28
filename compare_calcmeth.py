#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot
from include.tweegion_log import Tweegion as TweegionLog
from include.tweegion_lin import Tweegion as TweegionLin

blackwords = ["data/stoppwords200.txt"]
tweets = ["data/geo-tweets/unbalanced_175k.json"]
geo = ["data/geo-tweets/balanced-39k.json"]
loops = [0]
guesses = [0.2, 0.5, 0.6, 0.8]

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
					tweegion = TweegionRoot("geo",
	 					tweet,
	 					blackword,
	 					loop,
	 					geot,
	 					"",
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
					tweegion = TweegionLog("geo",
	 					tweet,
	 					blackword,
	 					loop,
	 					geot,
	 					"",
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
					tweegion = TweegionLin("geo",
	 					tweet,
	 					blackword,
	 					loop,
	 					geot,
	 					"",
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
