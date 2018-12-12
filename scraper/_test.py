from pytest import fixture


@fixture
def scraper_ob():
	from .scraper import getPosts
	return getPosts


def test_scraper(scraper_ob):
	li = scraper_ob('car', 1)
	assert len(li) > 0


