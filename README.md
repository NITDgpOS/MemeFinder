# Meme Retrieval Engine

## Collection
The memes are collected from popular subreddits using a scraper script
* File involved: `scrape/scraper.py`

## Standardization
The memes collected are put in `raw` folder and the script `standard.py` is run
* Each file name is extracted and stored in a text file next to the new hex based filename generated fot the image
* The standardized images are stored in the `processed` folder

## Usage
* To collect the memes from subreddits
```
sudo bash collect.sh
```
* The bash script prepares the database which allows the Meme Engine to function properly
*  To run the Meme Retrieval Engine (Meme Finder) type
```
sudo bash run.sh
```
* Enter the query in the text field and click on `Go`
* The memes are sorted based on relevance
* The selected memes can be browsed using the `Next` and `Previous` buttons


# Requirements
* OpenCV (cv2)
* Tesseract
* NLTK