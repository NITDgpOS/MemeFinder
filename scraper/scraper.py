import requests
from urllib.request import urlretrieve
import os
import sys
import time
import csv

counter = 0


def getPosts(subreddit, postLimit):
    url = 'http://www.reddit.com/r/{}/.json?limit={}'.format(subreddit, postLimit)
    headers = {
        'User-Agent': 'Reddit Wallpaper Scraper 1.0'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print('Sleeping for 2 seconds...\n')
        time.sleep(2)
        return data['data']['children']
    else:
        print('Sorry, but there was an error retrieving the subreddit\'s data!')
        return []


def saveImages(posts, scoreLimit, save_dir='reddit_wallpapers'):
    for post in posts:
        url = post['data']['url']
        score = post['data']['score']
        title = post['data']['title']
        if 'i.imgur.com' in url and score > scoreLimit:
            saveImage(url, title, save_dir)


def saveImage(url, title, save_dir):
    global counter
    try:
        save_dir = makeSaveDir(save_dir)
        dot_location = url.rfind('.')
        filename = (save_dir + title.replace('/', ':') +
                    url[dot_location: dot_location + 4])
        if not os.path.exists(filename):
            print('Saving ' + filename + '!\n')
            counter += 1
            urlretrieve(url, filename)
    except OSError:
        print('file name too long')


def makeSaveDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir + '/'


def downloadImagesFromReddit(subreddits, postLimit=1000, scoreLimit=100):
    for subreddit in subreddits:
        posts = getPosts(subreddit, postLimit)
        saveImages(posts, scoreLimit, subreddit.lower())
    print(str(counter) + ' images have been scraped!')


def main():
    if len(sys.argv) > 1:
        downloadImagesFromReddit(sys.argv[1:])
    else:
        with open('../scraper/Meme.csv', 'r') as f:
            reader = csv.reader(f)
            arr = [row[0] for row in reader]
            downloadImagesFromReddit(arr[:])


if __name__ == '__main__':
    main()
