# Meme Retrieval Engine

## Collection
The memes are collected from meme subreddits using a scraper script
* File involved: `scrape/scraper.py`

## Standardization
The memes collected are put in `raw` folder and the script `standard.py` is run
* Each file name is extracted and stored in a text file next to the new hex based filename generated fot the image
* The standardized images are stored in the `processed` folder

## Running
The Meme Retrieval Engine can now be run by running `meme_gui.py`
* The query is entered and the relevant memes can be easily browsed using the `Previous` and `Next` buttons