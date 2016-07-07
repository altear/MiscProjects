import nltk
import nltk.data

text = open('example.txt').read()

count = 0
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

extra_abbreviations = ['dr', 'vs', 'Mr', 'mrs', 'prof', 'inc', 'i.e'] 
sent_detector._params.abbrev_types.update(extra_abbreviations)

for sent in sent_detector.tokenize(text.strip()):
        print(str(count) + " : " + sent)
        count += 1


from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

for e in PunktParameters().abbrev_types:
	print(e)

punkt_param = PunktParameters()
punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc'])

for e in PunktParameters().abbrev_types:
	print(e)

sentence_splitter = PunktSentenceTokenizer(punkt_param)
text = "is THAT what you mean, Mrs. Hussey?"
sentences = sentence_splitter.tokenize(text)
print(sentences)

