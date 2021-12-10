import requests
from bs4 import BeautifulSoup
import datetime

#grabs urls from businesswire
def business_wire(driver, date_, homepage):
    urls = []
    response = requests.get(homepage)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_list = soup.find_all("div",{'itemscope':'itemscope'})
    ##clicking next button to load another page
    driver.get(homepage)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    button = driver.find_element_by_class_name("pagingNext")
    button.click()
    page_source = driver.page_source
    soup=BeautifulSoup(page_source, 'html.parser')
    div_list1 = soup.find_all("div",{'itemscope':'itemscope'})
    urls = []
    div_lists = [div_list, div_list1]
    for alist in div_lists:
        for story in alist:
            timestamp = (story.findChild('time'))['datetime']
            timestamp = datetime.datetime.strptime(timestamp,'%Y-%m-%dT%H:%M:%SZ')
            if timestamp > date_:
                urls.append( ( (story.findChild('a'))['href'], (story.findChild('span',{'itemprop':'headline'})).text ) ) 
    return urls