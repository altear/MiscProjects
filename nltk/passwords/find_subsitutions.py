from nltk.corpus import *
import time
import sys
import re
from multiprocessing import Pool
import multiprocessing
#save start time for user updates
start_time = time.time()
#parsed data, format is {word : count}
data = {}
#any lines that cannot be parsed
invalid_lines = []
#function for providing updates
def print_update(message):
	time_message = str(round(time.time()-start_time)) + 's'
	print("runtime: {:10}\t{}\n".format(time_message, message))

print_update("Parsing Input.")
#with open('data/Passwords/withcount/rockyou-withcount.txt', 'r', encoding="ISO-8859-1") as file:
#	for line in file.readlines():
#		try:
#			#we only need the second field
#			count, word = line.strip().split(' ')
#			data.append([word, count])
#		except:
#			invalid_lines.append(line)


print_update("Parsing Input2.")

def parse(val):
	return val.strip().split(' ')

def worker(lines):
	"""Make a dict out of the parsed, supplied lines"""
	result = []
	for line in lines:
		try:
			k, v = line.strip().split(' ')
			result.add([v, k])
		except:
			pass
		
	return result

with open('data/Passwords/withcount/rockyou-withcount.txt', 'r', encoding="ISO-8859-1") as infile:
	lines= infile.readlines()
	# configurable options.  different values may work better.
	numthreads = 8
	numlines = len(lines)
	# create the process pool
	pool = multiprocessing.Pool(processes=numthreads)
	# map the list of lines into a list of result dicts
	result_list = pool.map(worker, 
	(lines[line:line+numlines] for line in range(0,len(lines),numlines) ) )
	# reduce the result dicts into a single dict
	flattened = [val for sublist in result_list for val in sublist]
	print(len(flattened))



print_update("Finding English Words and Removing from Data.")
#english_words = set(w.lower() for w in words.words())
#print_update("Splitting words For Processing.")
