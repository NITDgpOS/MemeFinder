mkdir temp
mkdir raw
cd temp
python ../scraper/scraper.py
cd ..
mv temp/*/* raw/
rm -r temp
mkdir processed
python standard.py
python ocr.py