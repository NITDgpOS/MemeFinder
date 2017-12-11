import requests, urllib
import os, sys, time

counter = 0

def getPosts(subreddit, postLimit):
    url = 'http://www.reddit.com/r/' + subreddit + '/.json?limit=' + str(postLimit)
    headers = {
    'User-Agent': 'Reddit Wallpaper Scraper 1.0'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print('Sleeping for 3 seconds...\n')
        time.sleep(3)
        return data['data']['children']
    else:
        print('Sorry, but there was an error retrieving the subreddit\'s data!')
        return None

def saveImages(posts, scoreLimit, save_dir='reddit_wallpapers'):
    for post in posts:
        url = post['data']['url']
        score = post['data']['score']
        title = post['data']['title']
        if 'i.imgur.com' in url and score > scoreLimit:
            saveImage(url, title, save_dir)

def saveImage(url, title, save_dir):
    global counter
    save_dir = makeSaveDir(save_dir)
    dot_location = url.rfind('.')
    filename = (save_dir + title.replace('/', ':') + url[dot_location: dot_location + 4]).encode('utf-8')
    if not os.path.exists(filename):
        print('Saving ' + filename + '!\n')
        counter += 1
        urllib.urlretrieve(url, filename)

def makeSaveDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir + '/'

def downloadImagesFromReddit(subreddits, postLimit=100000, scoreLimit=10):
    for subreddit in subreddits:
        posts = getPosts(subreddit, postLimit)
        saveImages(posts, scoreLimit, subreddit.lower())
    print(str(counter) + ' images have been scraped!')

def main():
    if len(sys.argv) > 1:
        downloadImagesFromReddit(sys.argv[1:])
    else:
        downloadImagesFromReddit([
            'Memes',
            'Dankmemes',
            'surrealmemes',
            'MemeEconomy',
            'meme',
            'zuckmemes',
            'BrainMemes',
            'LeagueOfMemes',
            'MetalMemes',
            'fffffffuuuuuuuuuuuu',
            'treecomics',
            'gotfort',
            'catfort',
            'vertical',
            'adviceanimals',
            'inglip',
            'firstworldproblems',
            'fifthworldproblems',
            'HoldMyBeer',
            'politics',
            'blackpeopletwitter',
            'TheStopGirl',
            'OregonTrailProblems',
            'Pyongyang',
            'NotInteresting',
            'Terriblefacebookmemes',
            'NoNoNoNoYes',
            'YesYesYesYesNo',
            'OffensiveMemes',
            'Animemes',
            'animememes',
            'MortyMemes',
            'rickandmorty',
            'ilerminaty',
            'Conspiritards',
            'shittyadviceanimals',
            'meirl',
            'AdviceAnimals',
            'wholesomememes',
            'BikiniBottomTwitter',
            '2meirl4meirl',
            'dankchristianmemes',
            'indianpeoplefacebook',
            'IndianDankMemes',
            'ipfb',
            'DeepFriedMemes',
            'dank_meme',
            'wholesomebpt',
            'SuperShibe',
            'GarlicBreadMemes',
            'SpideyMeme',
            'ragecomics',
            'Memes_Of_The_Dank',
            'Harambe',
            'furry_irl',
            'wholesomegreentext',
            'MemesIRL',
            'CNNmemes',
            'nukedmemes',
            'billwurtzmemes',
            'AdviceAtheists',
            'Wholesome4chan',
            'Grimdank',
            'depression_memes',
            'Anti_Meme',
            'DankMemesFromSite19',
            'Dark_memes',
            'SadMemesForHipTeens',
            'MadMudmen',
            'RestaurantsThatMeme',
            'Patrig',
            'antimeme',
            'FreshMemes',
            'DatBoi',
            'TrollCoping',
            'wholesomestarterpacks',
            'meormyson',
            'dankcrusadememes',
            'BattlefrontMemes',
            'counterstrikememes',
            'CSGOmemes',
            'Meme_Battles',
            'MaymayZone',
            'IncrediblesMemes',
            'Jordan_Peterson_Memes',
            'vsaucememes',
            'pepethefrog',
            'interactivememes',
            'Chinese_Bootleg_Memes',
            'fishpost',
            'RoughRomanMemes',
            'Meme_Graveyard',
            'functionalmemes',
            'OnlyWholesomeMemes',
            'sadlygokarts',
            'ConfessionBear',
            'bioniclememes',
            'SuddenlyIRealized',
            'Antiquememes',
            'bgchatmemes',
            'TrueDank',
            'FlowerMemes',
            'MemeChimera',
            'TROLLXCOMMUNISM',
            'GrumpyCat',
            'SpaceyMemes',
            'allrages',
            'TrumpDraws',
            'dubaimemes',
            'TrumpMemes',
            'PoliticalHumor',
            'The_Donald',
            'Military',
            'militarymeme',
            'HistoryMemes',
            'CoaCOwtB',
            'BatmanSlap',
            'funny',
            'WonderWoman',
            'marvelmemes',
            'dcmemes'
        ])

if __name__ == '__main__':
    main()
