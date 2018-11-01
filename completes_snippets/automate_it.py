# -*- coding: utf-8 -*-
"""
Created on Nov 01

@author: vinimmelo

WebDriver automated test
"""

import requests
from lxml import html
import bs4
import re
import urllib3
import os
import urllib

def page_request():
    """
    inspeciona elementos de uma página com lxml (xpath)
    :return: Plans and Pricing of the site github.com/pricing
    """
    page = requests.get('https://github.com/pricing/')
    tree = html.fromstring(page.content)
    print("Page object:", tree)
    print("Page", page.url)
    plans = tree.xpath('//h2[@class="alt-h3"]/text()')
    pricing = tree.xpath('//span[@class="default-currency"]/text()')
    return print("Plans:", plans, "\nPricing:", pricing)


def parse_bs4():
    image_type = 'Project'
    movie = 'Avatar'
    url = "https://www.google.com/search?q="+movie+"&sourcelnms&tbm=isch"
    header = {'User-Agent': 'Mozilla/5.0'}
    http = urllib3.PoolManager()
    soup = bs4.BeautifulSoup(http.urlopen(http.request(method='Get', url=url, headers=header)))
    images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})][:5]
    for img in images:
        print ("Image Source:", img)

from selenium import webdriver
def webdriver_test():
    """
    Automatiza a abertura do navegador e cliques possíveis...
    :return: Login Facebook
    """
    browser = webdriver.Chrome()
    print("WebDriver object", browser)
    browser.maximize_window()
    browser.get('https://facebook.com')
    email = browser.find_element_by_name('email')
    swordfish = browser.find_element_by_name('pass')
    print ('Html elements')
    print ('Email: ', email, '\nPassword: ', swordfish)
    email.send_keys('viniciusmunizmel@yahoo.com.br') #envia o e-mail correto
    swordfish.send_keys('mudar') #envia a senha
    browser.find_element_by_id('loginbutton').click() #clica no login
    browser.implicitly_wait('5') #espera 5 segundos
    browser.save_screenshot('testeok.png') #tira um print...
    print(browser.current_url, browser.title)




if __name__ == '__main__':
    #print(requests.get("https://www.google.com/search?q=avatar&sourcelnms&tbm=isch").status_code)
    webdriver_test()
