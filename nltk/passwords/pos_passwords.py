#!/usr/bin/python3

import nltk
import sys
import time

from nltk import *
from nltk.corpus import *

start_time = time.time()

#with Passwords/withcount/rockyou-withcount.txt
data = {}
invalid_lines = []
datalist = []

def print_update(upt,stime=start_time):
	print("{t}s ...\n{msg}\n".format(t=round(time.time()-stime), msg=upt))
	
print_update("Overhead parsing...")
with open('data/Passwords/withcount/rockyou-withcount.txt', 'r', encoding="ISO-8859-1") as file:
	lines = file.readlines()
	for line in lines:
		try:
			count, password = line.strip().split(' ')
			data.update({password : int(count)})
			datalist.append([password, int(count)])
		except:
			invalid_lines.append(line)



#sort list by count
sorted_datalist = sorted(datalist, key = lambda x: x[1], reverse = True)
print_update("Overhead parsing complete...")


def common_english_words():
	#swadesh has some of the most common english words
	most_common_words = set(swadesh.words('en'))
	#most common words that are found in dictionary
	most_common_words.intersection_update(data)
	print(most_common_words)

#mostly in chapter 3, this is pretty complicated stuff
def fun_with_wordnet():
	print(len(sorted_datalist))
	#Get English Words
	english_vocab = set(w.lower() for w in words.words())
	output_list = []
	print(len(english_vocab))
	#Loop through top results that are words
	for password, count in sorted_datalist:
		if password.isalpha() and password in english_vocab:
			#loop through synsets of words and store them
			for synset in wordnet.synsets(password):
				print("Word: '{word}'".format(word=password))
				#synonyms
				print(synset.lemma_names()) 
				#more specific
				print(synset.hyponyms())
				#more general
				for path in synset.hypernym_paths():
					print("\tpath")
					for hypernym in path:
						print("\t\t{hyp}: ".format(hyp=hypernym.name()) + ", ".join(hypernym.lemma_names()))
						print("\t\t\t" + str(hypernym.hyponyms()))
				
			#since its only for test
			break
		
	print('got here')
	print(output_list)

def re_fun():
	import re
	english_vocab = set(w.lower() for w in words.words())
	count=0
	def wordfollowedbynum(word):
		res = re.search('^([A-Za-z]+)[0-9]+$', word)
		if res:
			return res.group(1).lower() in english_vocab
		return False
	
	def wordproceededbynum(word):
		res = re.search('^[0-9]+([A-Za-z]+)$', word)
		if res:
			return res.group(1).lower() in english_vocab
		return False		
		
		
	print_update("Words followed by number")
	print(len([w for w in data if wordfollowedbynum(w)]))
	
	print_update("Words proceeded by number")
	print(len([w for w in data if wordproceededbynum(w)]))		

def combined_fun():
	import re
	english_vocab = set(w.lower() for w in words.words())
	
	def wordfollowedbynum(word):
		res = re.search('^([A-Za-z]+)[0-9]+$', word)
		if res:
			return res.group(1).lower() in english_vocab
		return False
	
	def wordproceededbynum(word):
		res = re.search('^[0-9]+([A-Za-z]+)$', word)
		if res:
			return res.group(1).lower() in english_vocab
		return False
	
	ls = [w for w, c in sorted_datalist if w.isalnum() and not w.isalpha() and not w.isdigit() and not wordfollowedbynum(w) and not wordproceededbynum(w)]
	print(ls[:10])
	
def multiword():
	import re
	english_vocab = set(w.lower() for w in words.words())
	def subword(word):
		#10 to 1 
		index = 0
		for i in range(len(word), 0, -1):
			index = i
			if word[:i] in english_vocab:
				break
		if index == 0 and len(word) > 1:
			return subword[index:]
		elif index == 0:
			return ''
		else:
			return word[:index] + ' ' + subword(word[index:])
	count = 0
	for word, c in sorted_datalist:
		#clean up
		cword = "".join([letter for letter in word if letter.isalpha()])
		sword = subword(cword)	
		if ' ' in sword:
			print(word + " : " + sword)
			count += 1	
		if count > 100:
			break
		
def replaced_middle():
	import re
	english_vocab = set(w.lower() for w in words.words())
	english_passwords = sorted([[w, c] for w, c in sorted_datalist if w in english_vocab], key=lambda x:x[1], reverse=True)
	print(len(english_passwords))
	regexs = [[w[0]+'.'*(len(w) - 2)+w[-1], w] for w,c in english_passwords[:100] if len(w) > 2]
	print(len(regexs))
	#create dictionary of regex : password
	regexs_worg = {}
	for regex, w in regexs: 
			if regex in regexs_worg:
				regexs_worg[regex] += ', ' + w
			else:
				regexs_worg[regex] = w
	print(len(regexs_worg))
	
	#create dictionary of regex : replaced password
	rep_words = {}
	for p in data:
		for regex in regexs_worg:
			if len(p) == len(regex) and re.match(regex, p):
				if regex in rep_words:
					rep_words[regex] += ', ' + p
				else:
					rep_words[regex] = p
				break
		if round(time.time() - start_time) % 10:
			print("10 more seconds have passed, now on: " + p)
	#join dictionaries
	with open('replaced_middle_matches.txt', w) as output:
		for k in rep_words:
			print(regexs_worg[k] + '  :  ' + rep_words[k])

def replace_letter():
	import re
	english_vocab = set(w.lower() for w in words.words())
	english_passwords = sorted([[w, c] for w, c in sorted_datalist if w in english_vocab], key=lambda x:x[1], reverse=True)

	print_update("Creating regexs from most common words found in passwords")
	regexs = []
	for w, c in english_passwords[:100]:
		for letter in w:
			regexs.append([w.replace(letter,'.'), w])
	print_update("regex creation complete, {c} were made".format(c=len(regexs)))
	
	regexs_word = {}
	for r, w in regexs:
		if r in regexs_word:
			regexs_word[r] += ', ' + w
		else:
			regexs_word[r] = w
	print_update("reduced regex's to {c} unique values".format(c=len(regexs_word)))
	
	matches = {}
	ldata = len(data)
	count = 0
	printed = False
	print_update("Beginning to search...")
	search_start=time.time()
	oldmatches = set()
	for p in data:
		for r in regexs_word:
			if len(p) == len(r) and re.match(r, p) and not p in english_passwords:
				if r in matches:
					matches[r]+=', '+p
				else:
					matches[r] = p
				break
		count+=1
		if not round(time.time() - search_start) % 10:
			if not printed:
				print_update("{t}s: {c} / {l}, matches found: {lm}, eta: {eta}s\nNew matches: {mtch}".format(
					t=round(time.time() - search_start), 
					c=count, 
					l=ldata,
					lm=sum([len(values.split(', ')) for values in matches.values()]), 
					eta=round(time.time() - search_start)*ldata/count - time.time() - search_start,
					mtch=', '.join(set(matches).difference(oldmatches))),
					stime=search_start)
				printed=True
				oldmatches=set(matches)
		else:
			printed=False 
	 
	with open('replaced_letter_matches.txt', w) as output:
		for k in rep_words:
			print(" : ".join([k, regexs_worg[k], rep_words[k]]), file=output)
		
replace_letter()
#replaced_middle()
#multiword()			
#combined_fun()
#re_fun()
#fun_with_wordnet()
#common_english_words()

print("--- %s seconds ---" % (time.time() - start_time))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.25, 400))
