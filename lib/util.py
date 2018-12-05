from .search import get_score, create_index, generate_query

source = 'data2.txt'


def getMemes(query):
    """ Gets list of meme files from the database based on the query. """
    memes = get_score(create_index(source), generate_query(query))
    return memes
