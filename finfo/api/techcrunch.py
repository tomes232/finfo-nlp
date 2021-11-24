import calendar
import re
import requests
import bs4
from bs4 import BeautifulSoup
import time
# importing webdriver from selenium
import subprocess
from pathlib import Path
import selenium
import selenium.webdriver
import datetime
from datetime import date

def techcrunch(driver, date_):
    driver.get('https://techcrunch.com')
    button = driver.find_element_by_class_name("load-more")
    button.click()
    time.sleep(3)
    button.click()
    time.sleep(3)
    button.click()
    page_source = driver.page_source
    soup1=BeautifulSoup(page_source, 'html.parser')
    articles = soup1.find_all('article',class_ = 'post-block post-block--image post-block--unread')
    #print(articles)
    urls = []
    for article in articles:
        timestamp = datetime.datetime.strptime(article.findChild('time')['datetime'],'%Y-%m-%dT%H:%M:%S')
        #print(timestamp)
        if timestamp > date_:
            urls.append( (article.findChild('a')['href'], article.findChild('a').text))
    #for url in urls:
    #   print(url[0])
    return urls