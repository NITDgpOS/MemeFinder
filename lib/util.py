from .search import get_score, create_index, generate_query

source = 'database/data2.txt'


def get_memes(query):
    """ Returns list of meme files from the database based on the `query`. """
    memes = get_score(create_index(source), generate_query(query))
    memes = list(map(
        lambda e: e.replace('processed/', ''), memes
    ))
    return memes
