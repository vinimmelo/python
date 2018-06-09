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


if __name__ == '__main__':
    #print(requests.get("https://www.google.com/search?q=avatar&sourcelnms&tbm=isch").status_code)
    parse_bs4()