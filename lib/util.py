from .search import get_score_db, generate_query_db

def get_memes(query):
    """ Returns list of meme files from the database based on the `query`. """

    memes = get_score_db(generate_query_db(query))
    memes = list(map(
        lambda e: e.replace('processed/', ''), memes
    ))
    return memes
