#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion
from include.tweegion_root import Tweegion as TweegionRoot
from include.tweegion_log import Tweegion as TweegionLog
from include.tweegion_lin import Tweegion as TweegionLin

# tweegion = Tweegion("geo",
#  					"data/geo-tweets/balanced-39k.json",
#  					"data/stoppwords200.txt",
#  					0,
#  					"data/geo-tweets/unbalanced_175k.json",
#  					"")
# tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

# tweegion = TweegionLin, TweegionRoot ...
tweegion = Tweegion("regio",
 					"data/regio-tweets/scheffler_regio_corpus.json", # data/regio-tweets/regio_word_corpus.json
 					"data/stoppwords200.txt",
 					0, # Loops = 0,1,2,3,4,5,10,15,20
 					"",
 					"data/regionalwords.csv",
 					0.6) #Schaetzung: 0.9999999, 0.9, 0.5

#  nohup python compare_calcmeth.py > compare_calcmeth.results &
