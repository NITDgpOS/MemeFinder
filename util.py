from ..search import getScore, create_index, generateQuery

source = 'data2.txt'


def getMemes(query):
    getScore(create_index(source), generateQuery(query))
