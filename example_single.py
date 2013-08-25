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
 					0.99 )
#tweegion.evaluate_accuracy("data/geo-tweets/gold.json")
print tweegion.classify("Ich glaube @Drahflow tippt noch schneller als er redet. ;) #om13")