from numpy import *

def count_hits(gold_list,result_list):
	a = zeros((7,7), dtype=int8)
	for g,r in zip(gold_list, result_list):
		a[g][r] += 1
	return a

def confusion_table(hit_table):

    """Returns a confusion table in the following format:
    [true positives, false negatives,false positives, true negatives]
    for each region .

    This code was taken from:
    http://en.wikipedia.org/wiki/Confusion_matrix
    and modified by Steve Wendler

    """
    a = zeros((7,4), dtype=int8)
    for row in xrange(len(hit_table)):
	    predicted = hit_table[row]
	    actual = [hit_table[i][row] for i in range(len(hit_table))]
	    true_pos = predicted[row]
	    false_pos = sum(actual) - true_pos
	    false_neg = sum(predicted) - true_pos
	    total = sum([sum(i) for i in hit_table])
	    true_neg = total - true_pos - false_pos - false_neg
	    a[row] = [true_pos, false_neg,false_pos, true_neg]
    return a
		
def average_axis(a):
	return a.sum(axis = 0)/ float(len(a))

def recall(a):
	# calculates recall
	# true_pos/ (true_pos + false_neg)
	if a[0] != 0:
		return a[0]/float(a[0] + a[1])
	else:
		return 0

def precision(a):
	if a[0] != 0:
		return a[0]/ float(a[0] + a[2])
	else:
		return 0


# example

g = [0,1,2,3,4,5,6,0,0,0] # goldstandard
r = [0,1,2,3,6,0,6,0,1,5] # erzielte ergebniss

hit_table = count_hits(g,r)
cft = confusion_table(hit_table)
print g, " Goldstandard"
print r, " Ergbnissliste"
print "[true positives, false negatives,false positives, true negatives]"
print cft

# Recall und Precison fuer jede Region
for each in cft:
	print "Recall: ", recall(each), " precision: ", precision(each)

# Recall und Precision im Schnitt
print "durchschnittlicher Recall: ", recall(average_axis(cft))
print "durchschnittliche Precision: ", precision(average_axis(cft))
