mkdir temp
mkdir raw
mkdir processed
mkdir database

cd temp
python ../scraper/scraper.py
RESULT=$?
cd ..

if [ $RESULT -eq 0 ]; then
    mv temp/**/* raw/
    python scraper/standard.py && \
    python scraper/ocr.py && \
    rm -r temp && \
    rm -r raw
else
  echo "Stopping script!"
fi
