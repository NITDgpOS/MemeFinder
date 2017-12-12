# Meme Retrieval Engine
Author: Aniq Ur Rahman : @Aniq55 (GitHub, GitLab, BitBucket)

## Collection
The memes are collected from popular subreddits using a scraper script `scrape/scraper.py`

## Standardization
* The memes collected are put in `raw` folder and the script `standard.py` is run
* Each file name is extracted and stored in a text file next to the new hex based filename generated fot the image
* The standardized images are stored in the `processed` folder

## Query Extraction
* The entered query is split into words and synonyms for each word is added to the list of `related queries`
* We scan the database to match words with the words in `related queries` 
* This broadens the search area and minimizes zero output scenarios

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
* Pickle

# Future Improvements
* Adding functionality to the progress bar
* Adding feature to flush stored memes
* Creating an option to enter the names of subreddits to scrape from
* Storing popular meme templates and checking images for similarity and associating special keywords
