""" Game 2048, can achieve more than 1000 points!!! """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()

def game2048():
    """Game 2048"""
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
d
