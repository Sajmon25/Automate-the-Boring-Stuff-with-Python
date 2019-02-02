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
    # TODO: Find the URL of the comic image.

    # TODO: Download the image.

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done')