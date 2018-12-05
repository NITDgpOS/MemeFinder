from search import getScore, create_index, generateQuery

source = 'data2.txt'


def getMemes(query):
    """ Gets list of meme files from the database based on the query. """
    memes = getScore(create_index(source), generateQuery(query))
    return memes
