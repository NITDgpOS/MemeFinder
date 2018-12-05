from search import getScore, create_index, generateQuery

source = 'data2.txt'


def getMemes(query):
    memes = getScore(create_index(source), generateQuery(query))
    memes = list(map(
        lambda e: e.replace('processed/', 'memes/'),
        memes
    ))
    return memes
