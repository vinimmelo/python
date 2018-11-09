#!/usr/bin/env python
# Created on 08 November 2018
# @author vinimmelo
# Web automation, for scripting purposes. Working!

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


def game2048():
    #more than 1000 points
    browser.get('https://play2048.co/')
    sleep(3)
    b = browser.find_element_by_tag_name('html')
    for i in range(1000):
        b.send_keys(Keys.UP)
        sleep(1)
        b.send_keys(Keys.RIGHT)
        sleep(1)
        b.send_keys(Keys.DOWN)
        sleep(1)
        b.send_keys(Keys.LEFT)
        sleep(1)
    browser.quit()

if __name__ == '__main__':
    game2048()
