#!/usr/bin/env python
# Created on 05 November 2018
# @author vinimmelo
# Open websites in new tabs.

import webbrowser
import logging, time
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

sites = ['https://www.icloud.com',
         'https://www.wunderlist.com',
         'https://github.com',
         'https://nestle.facebook.com/',
         'https://translate.google.com/?hl=pt-BR',
         ]

def open_websites():
    logging.info('Beggin to Open Websites')
    for site in sites:
        webbrowser.open(site)
        logging.info(site)
        time.sleep(3)

if __name__ == '__main__':
    open_websites()
