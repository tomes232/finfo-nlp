
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
class ma_deal:
    summary = ""
    url = ""
    valuation = ""
    def __str__(self):
        string = "Summary: {}\nUrl: {}\nValuation: {}".format(self.summary,self.url,self.valuation)
        return string
def ma_parser(head,urls):
    ma_list = []
    keywords = ['acquisition', 'takeover','acquire','target','billion','million','$']
    for url in urls:
        #print(url)
        if any(x in url[0].lower() for x in keywords):
            url_ = head+url[0]
            response = requests.get(url_)
            soup = BeautifulSoup(response.text, 'html.parser')
            text_list = ['asdasasd. asdasd']
            if 'techcrunch' in head:
                mydiv = soup.find("div", {"class": "article-content"})
                text = mydiv.text
                text_list = text.split('\n')
                text_list = list(filter(None,text_list))
            elif 'prn' in head:
                mydiv = soup.find("section",{'class':'release-body container'})
                text = (mydiv.text).split('\n')
                text_list = list(filter(None,text))
            elif 'businesswire' in head:
                mydiv = soup.find("div",{'class':'bw-release-story'})
                if mydiv == None:
                    continue
                text = (mydiv.text).split('\n')
                text_list = list(filter(None,text))
            elif 'vcnews' in head:
                ##two instances of the same tag
                mydiv = (soup.find_all('div',{'class':'fullArticle'}))[1]
                #print(mydiv.text)
                text = (mydiv.text).split('\n')
                #print(text)
                text_list = list(filter(None,text))
            if 'vcnews' in head:
                summary = (soup.find("div",{'class':'summary mt-4 mb-2','id':'summary'})).text
            else:
                summary = text_list[0]
                del text_list[0]
            ma = ma_deal()
            valuation = []
            for text in text_list:
                sentences = text.split('. ')
                #print(sentence)
                for sentence in sentences:
                    if 'valuation' in sentence or 'valued' in sentence or '$' in sentence:
                        #print(sentence)
                        valuation.append(sentence)
            ma.url = url_
            ma.summary = summary
            ma.valuation = valuation
            ma_list.append(ma)
    string = ""
    for x in ma_list:
        string = string + str(x) + '\n\n'
    return string