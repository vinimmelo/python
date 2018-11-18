#!/usr/bin/env python
# Created on 05 November 2018
# @author vinimmelo
# Go to the address writed on command line or that is in the clipboard (copied).
# Very useful to turn this tedious thing in a cool one.

import webbrowser, sys, pyperclip

def main():
    if len(sys.argv) > 1:
        print("worked!")
        address = ' '.join(sys.argv[1:])
    else:
        print('Zero arguments!')
        address = pyperclip.paste()
    webbrowser.open(r'https://www.google.com/maps/place/' + address)


if __name__ == '__main__':
    main()
