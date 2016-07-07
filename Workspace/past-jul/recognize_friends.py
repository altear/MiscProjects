#!/usr/bin/python3


import nltk
import nltk.data

with open("dracula.txt") as file:
	text = file.read()

#Split into sentences
#for sent in nltk.sent_tokenize(text):

#Split into words
words = nltk.word_tokenize(text)
	
#Tag words with POS (Part of Speech)
tagged_words = nltk.pos_tag(words)
	
#Attain higher level 'chunks'
chunks = nltk.ne_chunk(tagged_words)

#Loop through each node
for node in chunks:
	#People are stored in Trees.
	#Check if this node is a tree, then check if the tree is a person (hah.)
	if type(node) is nltk.Tree and node.label() == "PERSON":
		#This little leaf was a person
		print(node.leaves()[0][0])

print("\n")

names =  set(node.leaves()[0][0] for node in chunks if type(node) is nltk.Tree and node.label() == "PERSON")
print(names)
