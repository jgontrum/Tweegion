#/usr/bin/ python
# -*- coding: utf8 -*-

from include.tweegion import Tweegion

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-8787.json",
					"data/stpwds_no_happytok.txt",
					3,
					"data/geo-tweets/balanced-3000.json",
					"")

print tweegion.classify("Dies ist ein ziemlich neutraler Beispieltweet.")