import nltk
from nltk.corpus import wordnet

try:
    from .models import *
except:
    pass

try:
    from models import *
except:
    pass

def generate_query_db(query):
    create_index_db()
    queryList = (' '.join(("".join((char if char.isalpha() else ' ')
                                   for char in query)).split(','))).split()
    keywords = []
    for query in queryList:
        for syn in wordnet.synsets(query):
            for l in syn.lemmas():
                keywords.append(l.name().lower())
    return keywords

def create_index_db(): 
    if not update_required :
        return
    ''' Creates index for the processed images '''
    data_db = db('post_ocr')
    index_db = db('INDEX')

    dropCollection('INDEX')
    data = data_db.find({})
    for entry in data:
        all_words = entry['attributes']+(entry['ocr_out'])

        words = (" ".join(("".join((char if char.isalpha() else " ")
            for char in (all_words )).split(','))).split())
        input_data = {
            'location' : entry['location'],
            'words' : words,
            'score' : 0
        }
        index_db.insert_one(input_data)

def get_score_db(keywords):
    index_db = db('INDEX')
    rows = index_db.find({})

    for row in rows:
        for word in row['words']:
            for key in keywords:
                if word.lower() == key.lower() :
                    index_db.update_one({'location': row['location'] }, {'$inc': {'score': 1 }})

    rows = index_db.find().sort([("score", pymongo.DESCENDING)])
    memememes = list( img['location'] for img in rows if img['score']>0 )
    # self obsession with me :P

    rows = index_db.find({})
    index_db.update_many({}, {'$set': {'score':0}})
    return memememes

def update_required():
    data_db = db('post_ocr')
    index_db = db('INDEX')

    processed_images = data_db.count()
    indexed_images = index_db.count()

    return processed_images != indexed_images