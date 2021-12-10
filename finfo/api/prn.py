import calendar
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date

#grabs urls from PR Newswire
def prn(url, date_):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    articles = soup.find('div',class_='col-md-8 col-sm-8 card-list card-list-hr')
    articles = articles.findChildren('div',class_='row')
    urls = []
    for article in articles:
        #print(article)
        timestamp = article.findChild('small').text
        #print(timestamp)
        timestamp = timestamp.split(',')
        if len(timestamp) == 1:
            ##formatting where its only hour
            today = date.today()
            day = today.day
            month = today.month
            year = today.year
            hour = 0
        else:
            month = list(calendar.month_abbr).index(((timestamp[0].split(' '))[0]))
            day = int((timestamp[0].split(' '))[1])
            year = int(timestamp[1])
            hour = int(((timestamp[2].strip(' ')).split(':'))[0])
        timestamp = datetime.datetime(year,month,day,hour,0,0)
        '''
        month = timestamp.split(' ')[0]
        month_num = 
        timestamp = re.sub("[^0-9]","-",timestamp)
        timestamp = str(month_num) + '-' + timestamp 
        print(timestamp)
        '''
        #print(timestamp)
        if timestamp > date_:
            urls.append( (article.findChild('a',class_='newsreleaseconsolidatelink display-outline')['href'],article.text))
    return urls