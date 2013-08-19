#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_log import Tweegion as TweegionLog

# ~~~~~~~~~~~~~~
tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					0,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					1,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					3,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

# ~~~~~~~~~~~~~~
tweegion = TweegionLog("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					0,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = TweegionLog("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					1,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = TweegionLog("geo",
					"data/geo-tweets/balanced-61k.json",
					"data/stoppwords200.txt",
					3,
					"data/geo-tweets/balanced-39k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")




