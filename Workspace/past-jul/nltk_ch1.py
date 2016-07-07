from nltk.book import *
from nltk import *

texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]

print("\nCommon Contexts")
for text in texts:
	text.common_contexts(["monstrous", "very"])

print("\nLength Texts")
for text in texts:
	print(str(len(text)) + " words in " + text.name) 

print("\nUnique words")
for text in texts:
	print(str(len(set(text))) + " unique words in " + text.name)

print("\nCount of 'The'")
for text in texts:
	print(str(text.count("the")) + " instances of 'the' in " + text.name)

print("\nLast Word")
for text in texts:
	print(sorted(text)[-5:])

print("\nFrequency Distribution")
for text in texts:
	print(FreqDist(text).most_common(5))

print("\nFirst index of word")
for text in texts:
	word = FreqDist(text).most_common(1)[0][0]
	print(str(text.index(word)) + " is first index of " + word)

print("\nExperiment for similar and common contexts..")
word = FreqDist(text5).most_common(40)[-1][0]
print("\nword = " + word)
similar = text5.similar(word)

print("\nCollocations and Bigrams")
words = [word[0] for word in FreqDist(text).most_common(20)[-5:]]
print(list(bigrams(words)))

