#   _  _   ___  _____  __      __ ___   ___  _  __ ___  _  _   ___
#  | \| | / _ \|_   _| \ \    / // _ \ | _ \| |/ /|_ _|| \| | / __|
#  | .` || (_) | | |    \ \/\/ /| (_) ||   /| ' <  | | | .` || (_ |
#  |_|\_| \___/  |_|     \_/\_/  \___/ |_|_\|_|\_\|___||_|\_| \___|
#
# Reddit has removed this API endpoint.
# READ: https://www.reddit.com/r/redditdev/comments/8gmf9v/api_receiving_404_when_hitting_get_subreddits_by/

import requests
import json
import sys
import shutil
import csv


for arg in sys.argv[1:]:
    print(arg)
    data = {
        'query': arg
    }
    headers = {
        'User-Agent': 'MemeFinder 1.0'
    }
    response = requests.get(
        "https://www.reddit.com/api/subreddits_by_topic.json",
        params=data,
        headers=headers
    )
    res = response.json()
    print(res)
    with open('scraper/Meme1.txt', 'ab+') as g:
        with open("scraper/Meme.txt", 'r+') as f:
            for line in f:
                line = line.strip()
                g.write(bytes(line + '\n'))
        for r in res:
            k = 0
            with open("scraper/Meme.txt", 'r') as f:
                msg = f.read().split(',')
                for i in range(0, len(msg)):
                    if r['name'] == msg[i].strip():
                        k = k + 1
                if k == 0:
                    g.write(bytes(',\n' + r['name']))
shutil.move('scraper/Meme1.txt', 'scraper/Meme.txt')
