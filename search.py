import nltk
from nltk.corpus import wordnet
import pickle


from bs4 import BeautifulSoup
import urllib2


# Generated extended related queries based on the user query
def generateQuery(query):
	queryList= (" ".join(("".join((char if char.isalpha() else " ") for char in query)).split(','))).split()
	keywords = []
	for query in queryList:
		for syn in wordnet.synsets(query):
		    for l in syn.lemmas():
		        keywords.append(l.name())
	#print(keywords)

	if(len(keywords)==0):
		print("sorry not present in dictionary")
		#web scrape the word store it in a variable



		internet_slang_you_want_to_search=query
		url='http://onlineslangdictionary.com/meaning-definition-of/'+str(internet_slang_you_want_to_search)

		page=urllib2.urlopen(url)

		soup=BeautifulSoup(page.read(), "html.parser")

		text=soup.find(class_="definitions").get_text()

		words = text.split()
		'''
		for word in words:
		    print(word)
		'''
		    

		for k in range(len(words)):
		    if(words[k][0]=='"'  ) :
		        i=k
		        #print(i)
		    if(words[k][-1]=='"' or words[k][-2]== '"'):
		        j=k
		        #print(j)
		        break

		words[i]=words[i][1:]

		if (words[j][-2]=='"'):
		    words[j]=words[j][0:-2]
		else:
		    words[j]=words[j][0:-1]



		fetched=words[i:j+1]

		print(fetched)
		#query=get the full sentence of lmao
		#queryList= (" ".join(("".join((char if char.isalpha() else " ") for char in query)).split(','))).split()

		for query in fetched:
			for syn in wordnet.synsets(query):
			    for l in syn.lemmas():
			        keywords.append(l.name())

        print(keywords)
	return keywords

# Creates a dictionary of file name and associated text attribues from the database
def create_index(database):
	db= open(database, 'r')
	INDEX={}
	db.readline()	# ignoring the column headers
	for entry in db:
		entry= entry.split(',')
		filename= entry[0]
		text= ' '.join(entry[1:])
		text= (" ".join(("".join((char if char.isalpha() else " ") for char in text)).split(','))).split()
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
			if word.lower() in [x.lower() for x in valueList[i]]:
				scoreList[i]= scoreList[i] +1
	score_file = open("score.pickle","wb")
	pickle.dump(scoreList, score_file)
	score_file.close()

	matched_files=[]
	for t in range(len(scoreList)):
		if scoreList[t] > 0:
			matched_files.append(keyList[t])

	while 0 in scoreList:
		scoreList.remove(0)

	matched={}
	l= len(scoreList)

	for i in range(l):
		matched[matched_files[i]]= scoreList[i]

	import operator
	sorted_list= sorted(matched.items(), key= operator.itemgetter(1))

	# return scoreList, matched_files
	memes= [ x[0] for x in sorted_list]
	return memes[::-1]

def load_index(index_name):
	index_file = open(index_name,"rb")
	return pickle.load(index_file)

# print(generateQuery(raw_input()))

# print(len(create_index("data3.txt")))

# print(getScore(create_index("data3.txt"), generateQuery('team sucks')))
