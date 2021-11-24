import requests
from bs4 import BeautifulSoup
def vc_parser(head,urls):
    article_texts = []
    keywords = [' round ', '$','bags','funding','raises','leads','series','seed','strategic','investment','invests','invest',]
    for url in urls:
        #print(url[0])
        if any(x in url[0].lower() for x in keywords):
            url_ = head+url[0]
            response = requests.get(url_)
            soup = BeautifulSoup(response.text, 'html.parser')
            if 'techcrunch' in head:
                #print(url_)
                article_title = (soup.find('h1',{'class':'article__title'})).text
                #print(article_title)
                mydiv = soup.find("div", {"class": "article-content"})
                text = mydiv.text
                text = text.replace('\n','')
                #text_list = list(filter(None,text))
                #print(text_list)
                #print()
                text = article_title + '. ' + text
                article_texts.append(text)
            elif 'prn' in head:
                #print(url_)
                if soup.find("div",{'class':'col-sm-8 col-vcenter col-xs-12'}) == None:
                    title = (soup.find("div",{'class':'col-sm-12 col-xs-12'}))
                    title = (title.findChildren("h1"))[0].text
                else:
                    title = soup.find("div",{'class':'col-sm-8 col-vcenter col-xs-12'}).text
                title = title.replace('\n','')
                mydiv = soup.find("section",{'class':'release-body container'})
                #text = (mydiv.text).split('\n')
                #text_list = list(filter(None,text))
                text = mydiv.text
                text = text.replace('\n','')
                text = title + '. ' + text
                article_texts.append(text)
            elif 'businesswire' in head:
                #print(url_)
                #print(response)
                #print(url_)
                if soup.find('h1',{'class':'epi-fontLg bwalignc'}) == None:
                    title = soup.find('h1',{'class':'epi-fontLg'})
                else:
                    title = (soup.find('h1',{'class':'epi-fontLg bwalignc'}))
                if not title.findChildren("b"):
                    title = title.text
                else:
                    title = (title.findChildren("b"))[0].text
                #print(title)
                mydiv = soup.find("div",{'class':'bw-release-story'})
                #print(mydiv)
                #text = (mydiv.text).split('\n')
                #text_list = list(filter(None,text))
                #print(mydiv.text)
                text = mydiv.text
                text = text.replace('\n','')
                text = title + '. ' + text
                article_texts.append(text)
            elif 'vcnews' in head:
                ##two instances of the same tag
                mydiv = (soup.find_all('div',{'class':'fullArticle'}))[1]
                #print(mydiv.text)
                text = (mydiv.text).split('\n')
                #print(text)
                text_list = list(filter(None,text))
                article_texts.append(text_list)
    return article_texts