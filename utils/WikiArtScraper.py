"""
really used in fetching url from wikiart
"""
from selenium import webdriver
import time
import os
import re
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
# os.environ["PATH"] += os.pathsep + 'D:\google-art-downloader-master'
chrome_options = Options()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options = chrome_options)

asserts_all=set()

mark_time = 0
last_value = 0


try:
    browser.get('https://www.wikiart.org/en/paintings-by-style/surrealism?select=featured#!#filterName:featured,viewType:masonry')
    while mark_time <= 5:
        pageSource = browser.page_source
        soup = BeautifulSoup(pageSource,'lxml')
        asserts = soup.find_all('img')
        for assert_value in asserts:
            if assert_value.get("src") != None and assert_value.get("src") != "":
                asserts_all.add(str(assert_value.get("src")).replace("!Large.jpg","").replace("!PinterestSmall.jpg",""))
#                 print(str(assert_value.get("src")).replace("!Large.jpg","").replace("!PinterestSmall.jpg",""))
        #     for assert_value in asserts:
        now_value = len(asserts_all)
        print(now_value)
        if last_value == now_value:
            mark_time += 1
        else:
            mark_time == 0
        try:
            browser.find_element_by_xpath('/html/body/div[2]/div[1]/section/main/div[4]/div/div/div[3]/a/span[3]').click()
        except Exception as e:
            print(e)
        last_value = now_value
        time.sleep(4)
    google_arts_images_urls = set()

    with open("wikiart_ink_and_wash_images_urls.txt",'w',encoding="utf8") as write_file:
        for line in asserts_all:
            write_file.write(line+"\n")
except Exception as e:
    print("global",e)
finally:
    browser.close()