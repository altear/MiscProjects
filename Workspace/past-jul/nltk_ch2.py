import nltk

from nltk import *
with open("dracula.txt") as f:
	tokens = nltk.word_tokenize(f.read())

text = nltk.Text(tokens)

alpha_text = [word for word in text if word.isalpha() and len(word) > 5 and 
word[0].isupper() and word[1:].islower()]
print(FreqDist(alpha_text).most_common(5))

from nltk.corpus import reuters, brown
print(brown.categories())
fileid = brown.fileids(brown.categories()[-1])
raw = brown.raw(fileid)
print(raw[:50])

cfd = nltk.ConditionalFreqDist(
	(genre, word)
	for genre in brown.categories()
	for word in brown.words(categories=genre))


