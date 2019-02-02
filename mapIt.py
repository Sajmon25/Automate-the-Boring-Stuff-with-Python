#! python3
# mapIt.py - Launches a map in the browser using and address from the command line or clipboard

import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
# TODO: Get address from clipboard

webbrowser.open('https://www.google.com/maps/place/' + address)

