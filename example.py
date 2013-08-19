#/usr/bin/ python
# -*- coding: utf8 -*-
from include.tweegion import Tweegion

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stpwds_no_happytok.txt",
					1,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stpwds_no_happytok.txt",
					2,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stpwds_no_happytok.txt",
					5,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stpwds_no_happytok.txt",
					10,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

# ~~~~~~~~~~~~~~

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords1000.txt",
					1,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords1000.txt",
					5,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

# ~~~~~~~~~~~~~~

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords500.txt",
					1,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords500.txt",
					5,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

# ~~~~~~~~~~~~~~

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords750.txt",
					1,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords750.txt",
					5,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

# ~~~~~~~~~~~~~~

tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords200.txt",
					1,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")


tweegion = Tweegion("geo",
					"data/geo-tweets/balanced-39k.json",
					"data/stoppwords200.txt",
					5,
					"data/geo-tweets/balanced-21k.json",
					"")
tweegion.evaluate_accuracy("data/geo-tweets/gold.json")

