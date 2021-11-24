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

def url_parser_prn(url):
    def num_there(s):
        return any(i.isdigit() for i in s)
    #url = 'https://www.prnewswire.com/news-releases/offchain-labs-rolls-out-arbitrum-one-ethereum-scaling-solution-to-the-public-and-announces-120m-in-funding-301365642.html'
    dic = {'series_round':'','series_amt':''}
    temp_string = url.split('/')
    words = temp_string[(len(temp_string)-1)].split('-')
    words = words[:-1]
    for x in range(0,len(words)-1):
        word = words[x]
        #print(word,end=" ")
        if num_there(word):
            #print(word)
            if dic['series_amt'] == '':
                if num_there(words[x+1]):
                    dic['series_amt'] = word + '.' + words[x+1]
                else:
                    dic['series_amt'] = word
                #print(dic)
        if word.lower() == 'series':
            dic['series_round'] = words[x+1]
    if dic['series_amt'] != '':
        temp = dic['series_amt'].strip('abcdefghigklmnopqrstuvwxyz')
        dic['series_amt'] = temp
    return dic