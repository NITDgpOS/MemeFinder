from pytest import fixture


@fixture
def op():
    from .util import get_memes
    return get_memes


def test_search(op):
		li = list(op('car'))
		assert len(li) > 0