#!/usr/bin/env python
"""
 Created on 08 November 2018
 @author vinimmelo
 Web automation, for scripting purposes. Working!

 """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()

def automation():
    browser.get('https://www.google.com/')
    sleep(5)
    browser.get('https://inventwithpython.com')
    try:
        elem = browser.find_element_by_link_text('More Info')
        elem.click()
        sleep(5)
        print('Found <%s> element with that class name!' % (elem.tag_name))
    except:
        print('Was not able to find an element with that name.')
    browser.quit() #maybe won't work


if __name__ == '__main__':
    automation()
