# Meme Retrieval Engine

[![Join the chat at https://gitter.im/MemeFinder/Lobby](https://badges.gitter.im/MemeFinder/Lobby.svg)](https://gitter.im/MemeFinder/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Author: __Aniq Ur Rahman__ | @Aniq55

![Demo](memefinder.png)
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
* Each file name is extracted and stored in a text file next to the new hex based filename generated fot the image
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

### Requirements
* cv2 (OpenCV)
* pytesseract
* nltk
* PIL
* hashlib
* shutil
* autocorrect
* pickle

### Future Improvements
* Adding functionality to the progress bar
* Correct the size scaling of memes for display on the canvas
* Adding feature to flush stored memes
* Creating an option to enter the names of subreddits to scrape from
* Storing popular meme templates and checking images for similarity and associating special keywords

## Documentation

### `standard.py`
* renames the memes present in `raw` folder to a  unique hex digest generated filename and moves it to `processed` folder

### `ocr.py`
* `extractText(image_path)`: extracts text using OCR from the meme at `image_path`

### `search.py`
* `generateQuery(query)`: Extends the query to include all synonyms related to the input query using nltk package
* `create_index(database)`: creates an dictionary (index) of all memes stored in the database, where the __filename__ is the `key` and the __associated text__ is the `value`
* `getScore(INDEX, keywords)`: Creates a relevance based score list matched with the filenames in `INDEX` for the given `keywords`
* `load_index(index_name)`: Loads an index dictionary from `index_name` using `pickle` library

### `meme_gui_support.py`
* `meme`: class which contains vital information like `memeList` and `currentImage` and the object of this class is very important in the functioning of the GUI
* `getMemeList(query)`: gets the list of memes which match the given `query`
* `display(canvas, image_path)`: displays the image at `image_path` on the `canvas` in the GUI
* `go(canvas, query)`: this function initiates all the process essential for the GUI to function. It gets the memeList ready based on the entered `query` and also dispays the first meme on the `canvas`
* `prev(canvas)`: displays the previous image on the `canvas`
* `next(canvas)`: displays the next image on the `canvas`
