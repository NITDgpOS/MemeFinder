# Memefinder Documentation

[Adding to documentation](./CONTRIBUTING.md)

**Table of Contents**

   * [Memefinder Documentation](#memefinder-documentation)
      * [Script: run.sh](#script-runsh)
      * [Script: add.sh](#script-addsh)
      * [Script: collect.sh](#script-collectsh)
      * [Script: tkrun.sh (DEPRECATED)](#script-tkrunsh-deprecated)
      * [Directory: lib/](#directory-lib)
         * [File: standard.py](#file-standardpy)
         * [File: ocr.py](#file-ocrpy)
         * [File: search.py](#file-searchpy)
            * [generate_query(query)](#generate_queryquery)
            * [create_index(database)](#create_indexdatabase)
            * [get_score(INDEX, keywords)](#get_scoreindex-keywords)
            * [load_index(index_name)](#load_indexindex_name)
         * [File: util.py](#file-utilpy)
            * [get_memes(query)](#get_memesquery)
         * [File: meme_gui.py (DEPRECATED)](#file-meme_guipy-deprecated)
         * [File: meme_gui_support.py (DEPRECATED)](#file-meme_gui_supportpy-deprecated)
            * [Class: meme](#class-meme)
            * [getMemeList(query)](#getmemelistquery)
            * [display(canvas, image_path)](#displaycanvas-image_path)
            * [go(canvas, query)](#gocanvas-query)
            * [prev(canvas)](#prevcanvas)
            * [next(canvas)](#nextcanvas)
      * [Directory: scraper/](#directory-scraper)
         * [File: api.py](#file-apipy)
         * [File: scraper.py](#file-scraperpy)
      * [Directory: database/](#directory-database)
      * [Directory: processed/](#directory-processed)
      * [Directory: raw/](#directory-raw)

---

## Script: `run.sh`

Runs the flask server on `localhost:5000` in development mode.

## Script: `add.sh`

Adds subreddits to the web scraping list.

## Script: `collect.sh`

Collects memes from the subreddits in `Meme.txt`.

## Script: `tkrun.sh` (DEPRECATED)

Runs the deprecated tkinter application.

---

## Directory: `lib/`

Contains the files required for searching through the database.

### File: `standard.py`

Renames the memes present in `raw/` folder to a unique hex-digest generated filename and moves it to `processed/` folder.

### File: `ocr.py`

Extracts text using Tesseract OCR from the meme from the `raw/` folder.

### File: `search.py`

#### `generate_query(query)`

Extends the query to include all synonyms related to the input query using nltk package.

#### `create_index(database)`

Creates an dictionary (index) of all memes stored in the database, where the **filename** is the `key` and the **associated text** is the `value`.

#### `get_score(INDEX, keywords)`

Creates a relevance based score list matched with the filenames in `INDEX` for the given `keywords`.

#### `load_index(index_name)`

Loads an index dictionary from `index_name` using `pickle` library.

### File: `util.py`

Used for the flask application.
Use the functions here for a higher level abstraction of the project.

#### `get_memes(query)`

Returns list of meme files from the database based on the `query`.

### File: `meme_gui.py` (DEPRECATED)

Starts the deprecated Tkinter GUI of the project.
Will be removed in the future.

### File: `meme_gui_support.py` (DEPRECATED)

Will be removed in the future.

#### Class: `meme`

Contains vital information like `memeList` and `currentImage` and the object of this class is very important in the functioning of the GUI.

#### `getMemeList(query)`

Gets the list of memes which match the given `query`.

#### `display(canvas, image_path)`

Displays the image at `image_path` on the `canvas` in the GUI.

#### `go(canvas, query)`

Initiates all the process essential for the GUI to function. It gets the memeList ready based on the entered `query` and also dispays the first meme on the `canvas`.

#### `prev(canvas)`

Displays the previous image on the `canvas`.

#### `next(canvas)`

Displays the next image on the `canvas`.

---

## Directory: `scraper/`

Contains files related to the web scraping part of the project.

### File: `api.py`

Finds a list of meme subreddits using reddit REST api. Stores the list in `scraper/Meme.txt`.

### File: `scraper.py`

Scraps meme images from the subreddits in `scraper/Meme.txt` and stores them in `processed/` directory.

**NOTE: Documentation Pending.** Need to document the functions.

---

## Directory: `database/`

Store for the txt-based comma separated databases.

## Directory: `processed/`

This is a store for image files with standardised file names.
*Will be created after running `collect.sh`*

## Directory: `raw/`

This is a store for image files from web scraping.
*Will be created after running `collect.sh`*
