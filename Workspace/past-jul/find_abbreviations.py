import nltk

with open("example.txt") as file:
	text = file.read()

sents = nltk.sent_tokenize(text)

parser = nltk.ChartParser(sents)
for tree in parser.parse(sents):
     print(tree)



