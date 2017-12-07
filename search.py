import nltk
from nltk.corpus import wordnet
import pickle

def search(query):
	queryList= "".join((char if char.isalpha() else " ") for char in query).split()

	keywords = []
	for query in queryList: 
		for syn in wordnet.synsets(query):
		    for l in syn.lemmas():
		        keywords.append(l.name())
	return keywords

def init_engine(database):
	db= open(database, 'r')
	INDEX={}
	for entry in db:
		entry= entry.split(',')
		filename= entry[0]
		text= (' '.join(entry[1:])).split()
		INDEX[filename]= text
	index_file = open("index.pickle","wb")
	pickle.dump(INDEX, index_file)
	index_file.close()

# print(search(raw_input()))

init_engine("data3.txt")