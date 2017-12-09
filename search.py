import nltk
from nltk.corpus import wordnet
import pickle


# Generated extended related queries based on the user query
def generateQuery(query):
	queryList= "".join((char if char.isalpha() else " ") for char in query).split()
	keywords = []
	for query in queryList: 
		for syn in wordnet.synsets(query):
		    for l in syn.lemmas():
		        keywords.append(l.name())
	return keywords

# Creates a dictionary of file name and associated text attribues from the database
def create_index(database):
	db= open(database, 'r')
	INDEX={}
	db.readline()	# ignoring the column headers
	for entry in db:
		entry= entry.split(',')
		filename= entry[0]
		text= (' '.join(entry[1:])).split()
		INDEX[filename]= text
	index_file = open("index.pickle","wb")
	pickle.dump(INDEX, index_file)
	index_file.close()
	return INDEX

# Scores each entry in the database on the basis of its relevance to the keywords
def getScore(INDEX, keywords):
	totalEntries= len(INDEX)
	keyList= INDEX.keys()
	valueList= INDEX.values()
	serialList= list(range(totalEntries))
	scoreList= [0 for i in range(totalEntries)]
	#Assigning score proportional to relevance
	for word in keywords:
		for i in range(totalEntries):
			if word in valueList[i]:	# matching to be made less strict
				scoreList[i]= scoreList[i] +1
	score_file = open("score.pickle","wb")
	pickle.dump(scoreList, score_file)
	score_file.close()
	return scoreList

# Loads an index dictionary
def load_index(index_name):
	index_file = open(index_name,"rb")
	return pickle.load(index_file)

# print(generateQuery(raw_input()))

# print(len(create_index("data3.txt")))

print(getScore(create_index("data3.txt"), generateQuery('sleep')))