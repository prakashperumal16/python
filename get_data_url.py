from turtle import title
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
from selenium import webdriver
import re

dr = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
dr.get("https://themakery.de/vegan-lip-and-cheek/Berlin")
soup = bs(dr.page_source,"lxml")

titles = [str(i.text).strip() for i in soup.find_all(class_='title txt_small marg-xxs-bottom')]
subTitles = [str(i.text).strip() for i in soup.find_all(class_='subtitle txt_medium min')]
print(titles)
print(subTitles[titles.index('Sprache')])


# language = [str(i.text).strip() for i in soup.find_all(class_='gallerypreview pgroup-0')]
# print(language)