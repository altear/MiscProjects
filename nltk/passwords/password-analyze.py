#!/usr/bin/python3

import nltk
import sys
import time

from nltk import *

start_time = time.time()

#with Passwords/withcount/rockyou-withcount.txt
with open('data/Passwords/withcount/rockyou-withcount.txt', 'r', encoding="ISO-8859-1") as file:
	data = []
	passwords_used_over_5 = []
	invalid_lines = []
	
	lines = file.readlines()
	for line in lines:
		try:
			count, password = line.strip().split(' ')
			count = int(count)
			data.append([count, password])
		
			if count > 5:
				passwords_used_over_5.append(password)
			
		except:
			invalid_lines.append(line)
	
	print("Number of passwords in dataset:")
	print(sum(sublist[0] for sublist in data))
       
	print("\nNumber of unique password names:")
	print(len(data))
	
	print("\nNumber of lines that could not be read:")
	print(len(invalid_lines))

	print("\nAverage length of password:")
	print(sum(count*len(password) for count, password in data)/sum(sublist[0] for sublist in data))
		
	print("\nMost common and least common passwords:")
	sorted_by_count = sorted(data, key = lambda item: item[0], reverse = True)
	print([item[1] for item in sorted_by_count[:10]])
	print([item[1] for item in sorted_by_count[-10:]])
	
	print("\nPasswords that are only alpha:")
	print(sum(count for count, password in data if password.isalpha()))
	
	print("\nPasswords that are only digits:")
	print(sum(count for count, password in data if password.isdigit()))
	
	print("\nPasswords that are not alphnum:")
	print(sum(count for count, password in data if not password.isalnum()))

	print("\nPasswords that are words:")
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	print(sum(count for count, password in data if password in english_vocab))
	
	print("Most common words used:")
	words_used = sorted([item for item in data if item[1].isalpha() and item[1] in english_vocab], key=lambda item: item[0], reverse = True)
	print(words_used[:10])
	
	words_used_nc = set(password for count, password in words_used)
	print("\ndo the most commmon words have their synsets also used?")
	
	passwords = [password for count, password in data]

	def multidim_index(ls, item):
		for subls in ls:
			if subls.index(item) != -1:
				return [ls.index(subls), subls.index(item)]
		return -1
		
	def most_popular_synset(word):
		synsets = nltk.corpus.wordnet.synsets(word)
		syn_words_and_passwords = []
		for synset in synsets:
			syn_words = synset.lemma_names()
			retlist = [data[passwords.index(w)] for w in syn_words if w in passwords]
			if not len(retlist):
				continue
			retlist.append(sum(count for count, password in retlist))
			syn_words_and_passwords.append(retlist)
		
		if len(syn_words_and_passwords):
			syn_words_and_passwords.append(word)
			syn_words_and_passwords.append(sum(row[-1] for row in syn_words_and_passwords if str(row[-1]) != word and str(row[-1]).isnumeric()))
		return syn_words_and_passwords
	
	synsets = [most_popular_synset(word[1]) for word in words_used[:100]]
	#remove empty
	synsets = [synset for synset in synsets if len(synset)]
	
	sort_syn = sorted(synsets, key=lambda item: item[-1], reverse = True)[:10] 
	for line in sort_syn:
		print(line[-2:])
	print("\nCOUP DE GRAS")
	#for synset in synsets:
	#	print(synset)
	
	names = set(w.lower() for w in nltk.corpus.names.words())
	male_names = set(w.lower() for w in nltk.corpus.names.words('male.txt'))
	female_names = set(w.lower() for w in nltk.corpus.names.words('female.txt'))
	print("Passwords that are names:")
	print(sum(count for count, password in data if password.isalpha() and password in names))
	
	print("Passwords that are male names:")
	print(sum(count for count, password in data if password.isalpha() and password in male_names))
	
	print("Passwords that are female names:")
	print(sum(count for count, password in data if password.isalpha() and password in female_names))
	
	print("Most common names used:")
	print(sorted([item for item in data if item[1].isalpha() and item[1] in names], key=lambda item: item[0], reverse = True)[:10])
	
print("--- %s seconds ---" % (time.time() - start_time))
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.25, 100))
#	print("There are " + str(len(passwords)) + " unique passwords in this list")

#	print("\nThe 20 most common passwords are:")
#	print(lines[:20])
#	
#	print("\nThe average length of password is:")
#	print(len(passwords[10]))
	#avglen = len(passwords)/sum(len(password) for password in passwords)

#	print("\nThe % of passwords with 5 or more characters")
#	print(str(passcount) + " / " + str(totalcount))
#	print(passcount/totalcount)

#	print("\nThe % of the 20 most common passwords") 
#	print(str(topn) + " / " + str(totalcount))
#	print(topn/totalcount)
