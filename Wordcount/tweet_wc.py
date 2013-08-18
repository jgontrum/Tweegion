import sys
import json
import operator
import pickle
import os
import codecs
lib_path = os.path.abspath('../include')
sys.path.append(lib_path)
from happyfuntokenizing import Tokenizer


def sort_dict(dictionary):
    i = sorted(dictionary.iteritems(), key=operator.itemgetter(1), reverse=True)
    stpwrds = codecs.open('stpwds2.txt','w','utf8')
    stpwrdscnt = codecs.open('stpwrdscnt2.txt', 'w','utf8')
    for e in i:
        if (e[1] > 100):
            #print e
                stpwrds.write(e[0] + '\n')
                stpwrdscnt.write('%7d  %s \n' % (e[1],e[0]))
        else:
            stpwrds.close()
            stpwrdscnt.close()
        exit()
    
def read_and_count():
    dictionary = {}
    tweetfolder = '/home/gontrum/april-corpus-raw'

    tok = Tokenizer(preserve_case=False)
    
    for tweetfile in [folder for folder in os.listdir(tweetfolder) if folder.startswith('tweets') == True ]:
        tweetfile = os.path.join(tweetfolder, tweetfile)
    with open(tweetfile, 'r') as f:
            for line in f:
                try:
                    tw = json.loads(line, 'latin1')['text']
                except:
                    None
                for each in tok.tokenize(tw):
                    dictionary[each] = dictionary.get(each, 0) + 1

    return dictionary

def serialize_dict(dictionary):
    with open('stpwrdsDict.txt','w') as f:
        pickle.dump(dictionary, f)

def read_in_dict():
    with open('stpwrdsDict.txt','r') as f:
        d = pickle.load(f)
    return d
        

#dictionary = read_and_count()
#serialize_dict(dictionary)

d = read_in_dict()
sort_dict(d) 