#/usr/bin/ python
# -*- coding: utf8 -*-

from include.tweegion import Tweegion

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stpwds_no_happytok.txt",
					1,
					"data/geo-tweets/balanced-21k.json",
					"")

# print tweegion.classify("Dies ist ein ziemlich neutraler Beispieltweet.", False)
# print tweegion.classify("Dies ist ein ziemlich neutraler Beispieltweet.", True)

tweegion.evaluate_accuracy("data/geo-tweets/gold.json")