import geo as geo_functions
from regions import regions as region_dict
geo = geo_functions.GeoFunctions()

counter = {"Norden" : 0, "Osten" : 0, "Westen" : 0, "Suedwest" : 0, "Bayern" : 0, "Oesterreich" : 0, "Schweiz" : 0}

test_data = open("geo_data.txt",'r')
for line in test_data:
	lang,lat = line.split(",")
	reg = geo.get_region((float(lang),float(lat)))
	if reg != "Not found":
		counter[reg] += 1  

print counter
