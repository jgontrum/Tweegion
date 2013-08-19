#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot

tweegion = TweegionRoot("geo",
 					"data/geo-tweets/balanced-61k.json",
 					"data/stoppwords200.txt",
 					0,
 					"data/geo-tweets/balanced-39k.json",
 					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = TweegionRoot("geo",
 					"data/geo-tweets/balanced-61k.json",
 					"data/stoppwords200.txt",
 					1,
 					"data/geo-tweets/balanced-39k.json",
 					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = TweegionRoot("geo",
 					"data/geo-tweets/balanced-61k.json",
 					"data/stoppwords200.txt",
 					3,
 					"data/geo-tweets/balanced-39k.json",
 					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


# ~~~~~~~~~~~~~~
tweegion = Tweegion("geo",
					"data/geo-tweets/unbalanced_175k.json",
					"data/stoppwords200.txt",
					0,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/unbalanced_175k.json",
					"data/stoppwords200.txt",
					0,
					"data/geo-tweets/unbalanced_175k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					0,
					"data/geo-tweets/unbalanced_175k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					0,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/unbalanced_175k.json",
					"data/stoppwords200.txt",
					1,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/unbalanced_175k.json",
					"data/stoppwords200.txt",
					1,
					"data/geo-tweets/unbalanced_175k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					1,
					"data/geo-tweets/unbalanced_175k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					1,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
# ~~~~~~~~~~~~~~

