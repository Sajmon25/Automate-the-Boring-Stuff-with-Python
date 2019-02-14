#! python3
# downloadXkcd.py - Download every single XKCD comic.

import requests
import os
import bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswitch('#'):
    # TODO: Download the page
    print('Download page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # TODO: Download the image.
            print('Downloading image %s...' % {comicUrl})
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done')