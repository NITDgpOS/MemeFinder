mkdir temp
mkdir raw
mkdir processed
mkdir database

cd temp
python ../scraper/scraper.py
RESULT=$?
cd ..

if [ $RESULT -eq 0 ]; then
    cp temp/*/* raw/
    python scraper/standard.py
    python scraper/ocr.py
else
  echo "Stopping script!"
fi
