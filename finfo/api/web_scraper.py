# importing webdriver from selenium
import subprocess
from pathlib import Path
import selenium
import selenium.webdriver
import datetime
from datetime import date
from finfo.api.vc import vc_parser
from finfo.api.business_wire import business_wire
from finfo.api.prn import prn
from finfo.api.techcrunch import techcrunch
from finfo.api.date_ import date_func
import json
import os
from dotenv import load_dotenv

from finfo.api.classification import classification
from finfo.api.genDatabase import genDatabase
from finfo.mongodb import upload_dict

load_dotenv()
PATH_TO_CHROMEDIRVER= "bin/chromedriver"

with open('finfo/api/config.json', 'r') as f:
    config = json.load(f)


def scraper():
    """this is the scraper"""
    print('hello')
    print(PATH_TO_CHROMEDIRVER)
    options = selenium.webdriver.chrome.options.Options()
    options.add_argument("--headless")

    # chromedriver is not in the PATH, so we need to provide selenium with
    # a full path to the executable.
    node_modules_bin = subprocess.run(
        ["npm", "bin"],
        stdout=subprocess.PIPE,
        universal_newlines=True,
        check=True
    )
    node_modules_bin_path = node_modules_bin.stdout.strip()
    chromedriver_path = PATH_TO_CHROMEDIRVER #Path(node_modules_bin_path) / "chromedriver"

    driver = selenium.webdriver.Chrome(
        options=options,
        executable_path=str(chromedriver_path),
    )
    date_ = date_func()
    bw_articles = business_wire(driver,date_,'https://www.businesswire.com/portal/site/home/news/subject/?vnsId=31355')
    head = 'https://www.businesswire.com'
    bw_vc = vc_parser(head,bw_articles)
    print('bw done')


    head = 'https://www.prnewswire.com'
    url = 'https://www.prnewswire.com/news-releases/financial-services-latest-news/venture-capital-list/?pagesize=50'
    prn_articles = prn(url,date_)
    #print(prn_articles)
    prn_vc = vc_parser(head,prn_articles)
    print('prn done')
    #prn_ma = ma_parser(head,ma_urls)
    head = 'https://techcrunch.com'
    tc_articles = techcrunch(driver,date_)
    tc_vc = vc_parser(head,tc_articles)
    print('tc done')

    driver.close()


    #final_string_ma = prn_ma + tc_ma + bw_ma
    final_list = prn_vc + tc_vc + bw_vc
    ## creating a new file each time
    with open('sandbox.jsonl', 'w') as jsonl_file:
            jsonl_file.write('')
    for article in final_list:
        ##print(article[0])

        article_classification = "funding"#classification(".".split(article)[0])
        #print(".".join(article.split(".")[:10]))
                
        data_dic = {"text": article, "metadata": str(date_.strftime('%Y-%m-%d'))}
        data_upload = {"text": article, "metadata": str(date_.strftime('%Y-%m-%d'))}

        dict_in = upload_dict(data_upload, "articles", article_classification)

        if article_classification == 'funding' and dict_in:
            company, db_entry = genDatabase(".".join(article.split(".")[:10]))
            db_entry["date"] = date_.strftime('%Y-%m-%d')
            db_entry["article_id"] = data_upload["_id"]

            upload_dict(db_entry, "companies", company)
        


        upload_dict(data_upload, "articles", article_classification)
        with open('sandbox.jsonl', 'w') as jsonl_file:
            #print(data_dic)
            json.dump(data_dic, jsonl_file)
            jsonl_file.write('\n')
    #print(final_string)
    # with open("ma.txt", "w") as ma_file:
    #     ma_file.write(final_string_ma)
# if __name__ == '__main__':
#     main()