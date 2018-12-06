import requests
import json
import sys
import shutil

for arg in sys.argv[1:]:
    data = {'query': arg}
    headers = {
        'User-Agent': 'MemeFinder 1.0'
    }
    response = requests.get(
        "https://www.reddit.com/api/subreddits_by_topic.json",
        params=data,
        headers=headers)
    res = response.json()
    with open('Meme1.txt', 'ab') as g:
        with open("Meme.txt", 'r') as f:
            for line in f:
                line = line.strip()
                g.write(bytes(line + '\n'))
        for r in res:
            k = 0

            f = open("Meme.txt", 'r')
            msg = f.read().split(',')
            for i in range(0, len(msg)):
                if r['name'] == msg[i].strip():
                    k = k + 1
            if k == 0:
                g.write(bytes(',\n' + r['name']))
            f.close()
shutil.move('Meme1.txt', 'Meme.txt')
