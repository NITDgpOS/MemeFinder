import nltk
from nltk.corpus import wordnet
import pickle
import os

DIRNAME = os.path.dirname(os.path.abspath(__file__))


def generate_query(query):
    """ Generated extended related queries based on the user query. """
    queryList = (' '.join(("".join((char if char.isalpha() else ' ')
                                   for char in query)).split(','))).split()
    keywords = []
    for query in queryList:
        for syn in wordnet.synsets(query):
            for l in syn.lemmas():
                keywords.append(l.name())
    return keywords


def create_index(database):
    """ Creates a dictionary of file name and associated text attribues from the database. """
    with open(database) as db:
        INDEX = {}
        db.readline()  # ignoring the column headers
        for entry in db:
            entry = entry.split(',')
            filename = entry[0]
            text = ' '.join(entry[1:])
            text = (' '.join((''.join((char if char.isalpha() else ' ')
                                      for char in text)).split(','))).split()
            INDEX[filename] = text
        with open(os.path.join(DIRNAME, 'index.pickle'), 'wb') as index_file:
            pickle.dump(INDEX, index_file)
    return INDEX


def get_score(INDEX, keywords):
    """ Scores each entry in the database on the basis of its relevance to the keywords. """
    total_entries = len(INDEX)
    key_list = list(INDEX.keys())
    valueList = list(INDEX.values())
    serial_list = list(range(total_entries))
    score_list = [0 for i in range(total_entries)]
    # Assigning score proportional to relevance
    for word in keywords:
        for i in range(total_entries):
            if word.lower() in [x.lower() for x in valueList[i]]:
                score_list[i] = score_list[i] + 1
    with open(os.path.join(DIRNAME, 'score.pickle'), 'wb') as score_file:
        pickle.dump(score_list, score_file)

    matched_files = []
    for t in range(len(score_list)):
        if score_list[t] > 0:
            matched_files.append(key_list[t])

    while 0 in score_list:
        score_list.remove(0)

    matched = {}
    l = len(score_list)

    for i in range(l):
        matched[matched_files[i]] = score_list[i]

    import operator
    sorted_list = sorted(matched.items(), key=operator.itemgetter(1))

    # Return score_list, matched_files
    memes = [x[0] for x in sorted_list]
    return memes[::-1]


def load_index(index_name):
    """ Returns an object from given pickle file. """
    with open(index_name, 'rb') as index_file:
        obj = pickle.load(index_file)
    return obj
