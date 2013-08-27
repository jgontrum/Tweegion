#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot
from include.tweegion_log import Tweegion as TweegionLog

tweegion = Tweegion("geo",
 					"data/geo-tweets/balanced-39k.json",
 					"data/empty.txt",
 					1,
 					"data/geo-tweets/unbalanced_175k.json",
 					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
