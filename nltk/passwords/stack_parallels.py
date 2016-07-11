from nltk.corpus import words
from multiprocessing import Pool
import math
import re
import time

regex = "^.*ll.*$"
english_words = [w.lower() for w in words.words()] * 30
print(len(english_words))

def findOccurance(word):
	return re.search(regex, word) is not None, word

start_time = time.time()
with open('filteredparallel.txt', 'w') as outlist:
	pool = Pool(processes=4)
	bincount = 10
	binsize = math.ceil(len(english_words) / bincount)
	#word_groups = [english_words[i:i+binsize] for i in range(0, len(english_words), binsize)]
	for ret,line in pool.map(findOccurance, english_words, chunksize=binsize):
		if ret:
			print(line, file=outlist)
	pool.close()
	
print("{:5}s".format(time.time()-start_time))
start_time = time.time()

with open('filterednormal.txt', 'w') as outlist:
	for ret, line in map(findOccurance, english_words):
		if ret:
			print(line, file=outlist)
	
print("{:5}s".format(time.time()-start_time))
start_time = time.time()

with open('filterednormal.txt', 'w') as outlist:
	for line in english_words:
		if re.search(regex, line):
			print(line, file=outlist)
			
			
print("{:5}s".format(time.time()-start_time))
	