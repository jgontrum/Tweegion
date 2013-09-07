#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot
from include.tweegion_log import Tweegion as TweegionLog
from include.tweegion_lin import Tweegion as TweegionLin


# executes the tweegion-alogorithm for the regio-word-attempt
# guesses are fixed to 20%
# stopwords are fixed to 200

# please execute in command-line: nohup python compare_regio_words.py > xxx.results &
blackwords = ["data/stoppwords200.txt"]
tweets = ["data/regio-tweets/regio_word_corpus.json", "data/regio-tweets/scheffler_regio_corpus.json", "data/regio-tweets/scheffler_regio_oneday.json"]
regios = ["data/regionalwords.csv"]
loops = [0,1,2,3,4,5,10,15,20]
guesses = [0.2]

for guess in guesses:
	for loop in loops:
		for blackword in blackwords:
			for tweet in tweets:
				for reg in regios:
					tweegion = Tweegion("regio",
	 					tweet,
	 					blackword,
	 					loop,
	 					"",
	 					reg,
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
					tweegion = TweegionRoot("regio",
	 					tweet,
	 					blackword,
	 					loop,
	 					"",
	 					reg,
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
					tweegion = TweegionLog("regio",
	 					tweet,
	 					blackword,
	 					loop,
	 					"",
	 					reg,
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
					tweegion = TweegionLin("regio",
	 					tweet,
	 					blackword,
	 					loop,
	 					"",
	 					reg,
	 					guess)
					tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
