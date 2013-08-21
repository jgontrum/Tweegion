#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot

tweegion = Tweegion("geo",
 					"data/geo-tweets/balanced-39k.json",
 					"data/stoppwords200.txt",
 					1,
 					"data/geo-tweets/balanced-61k.json",
 					"data/regionalwords.csv",
 					0.33 )
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = TweegionRoot("geo",
 					"data/geo-tweets/balanced-39k.json",
 					"data/stoppwords200.txt",
 					1,
 					"data/geo-tweets/balanced-61k.json",
 					"data/regionalwords.csv",
 					0.33 )
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
 					"data/geo-tweets/balanced-39k.json",
 					"data/stoppwords200.txt",
 					0,
 					"data/geo-tweets/balanced-61k.json",
 					"data/regionalwords.csv",
 					0.33 )
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = TweegionRoot("geo",
 					"data/geo-tweets/balanced-39k.json",
 					"data/stoppwords200.txt",
 					0,
 					"data/geo-tweets/balanced-61k.json",
 					"data/regionalwords.csv",
 					0.33 )
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

