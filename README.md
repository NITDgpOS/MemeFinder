# Meme Retrieval Engine

[![Join the chat at https://gitter.im/NIT-dgp/General](https://badges.gitter.im/MemeFinder/Lobby.svg)](https://gitter.im/NIT-dgp/General)

![Demo](docs/images/ss_flask.png)
## Project Description

### Technologies employed
* Image Processing
* Machine Learning
* Natural Language Processing
* Shell Scripting

### Collection
The memes are collected from popular subreddits using a scraper script `scrape/scraper.py`

### Standardization
* The memes collected are put in `raw` folder and the script `standard.py` is run
* Each file name is extracted and stored in a text file next to the new hex based filename generated for the image
* The standardized images are stored in the `processed` folder

### Query Extraction
* The entered query is split into words and synonyms for each word is added to the list of `related queries` using the nltk library
* We scan the database to match words with the words in `related queries` 
* This broadens the search area and minimizes zero output scenarios

### Relevance to query
* The memes are ordered in order of their relevance to the search query
* This is done by assigning a score to each meme present in the database and then sorting in descending order of scores

### Optical Character Recognition
* OCR is done using __Tesseract__ to extract text from the memes which is an essential part of the project
* The extracted text are not perfectly accurate so the output from ocr is fed into the spellchecker of the Python `autocorrect` library
* The spellchecker makes the conversion more accurate

### Quick Testing
To run the GUI and test the functionalities, simply type 
```
sudo bash run.sh
```

### Collect and Run
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

### Add new subreddits to the list 
```
sudo bash add.sh
```

### Requirements
* cv2 (OpenCV)
* pytesseract
* nltk
* PIL
* hashlib
* shutil
* autocorrect
* pymongo

### Future Improvements
* Adding functionality to the progress bar
* Correct the size scaling of memes for display on the canvas
* Adding feature to flush stored memes
* Storing popular meme templates and checking images for similarity and associating special keywords

## Documentation
[MemeFinder documentation](docs/README.md)
