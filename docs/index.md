Memefinder Documentation
========================

[Adding to documentation](./CONTRIBUTING.md)

-----

## Directory: `lib/`

This directory contains the files required for searching through the database.

### File: `standard.py`

Renames the memes present in `raw/` folder to a unique hex-digest generated filename and moves it to `processed/` folder.

### File: `ocr.py`

Extracts text using Tesseract OCR from the meme from the `raw/` folder.

### File: `search.py`

#### `generate_query(query)`

Extends the query to include all synonyms related to the input query using nltk package.

#### `create_index(database)`

Creates an dictionary (index) of all memes stored in the database, where the __filename__ is the `key` and the __associated text__ is the `value`.

#### `get_score(INDEX, keywords)`

Creates a relevance based score list matched with the filenames in `INDEX` for the given `keywords`.

#### `load_index(index_name)`

Loads an index dictionary from `index_name` using `pickle` library.

### File: `util.py`

This file is used for the flask application. Use the functions here for a higher level abstraction of the project.

#### `get_memes(query)`

Returns list of meme files from the database based on the `query`.

### File: `meme_gui.py` **(DEPRECATED)**

Starts the deprecated Tkinter GUI of the project.
Will be removed in the future.

### File: `meme_gui_support.py` **(DEPRECATED)**

Will be removed in the future.

#### Class: `meme`

Contains vital information like `memeList` and `currentImage` and the object of this class is very important in the functioning of the GUI.

#### `getMemeList(query)`

Gets the list of memes which match the given `query`.

#### `display(canvas, image_path)`

Displays the image at `image_path` on the `canvas` in the GUI.

#### `go(canvas, query)`

This function initiates all the process essential for the GUI to function. It gets the memeList ready based on the entered `query` and also dispays the first meme on the `canvas`.

#### `prev(canvas)`

Displays the previous image on the `canvas`.

#### `next(canvas)`

Displays the next image on the `canvas`.

