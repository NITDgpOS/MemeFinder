mkdir temp
mkdir raw
mkdir processed
mkdir database

cd temp
python ../scraper/scraper.py
RESULT=$?
cd ..

if [ $RESULT -eq 0 ]; then
    mv temp/*/* raw/
    rm -rf temp
    python scraper/standard.py
    python scraper/ocr.py
    rm -r raw/
else
  echo "Stopping script!"
fi
