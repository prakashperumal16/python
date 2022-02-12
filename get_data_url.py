from turtle import title
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
from selenium import webdriver
import re
import datetime

dr = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
dr.get("https://themakery.de/vegan-lip-and-cheek/Berlin")
soup = bs(dr.page_source,"lxml")
data_image = soup.find_all(class_='gallerypreview pgroup-0')
image_tag=[]
for image in data_image:
    image_tag.append(re.findall(r"'(.*?)'", image["style"], re.DOTALL)[0])
# service_image = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='gallerypreview pgroup-0')]
print(image_tag)
# titles = [str(i.text).strip() for i in soup.find_all(class_='title txt_small marg-xxs-bottom')]
# subTitles = [str(i.text).strip() for i in soup.find_all(class_='subtitle txt_medium min')]
# print(titles)
# print(subTitles[titles.index('Uhrzeit')])

# timeStr = subTitles[titles.index('Uhrzeit')].split('-')
# start_hour = timeStr[0].rstrip().split(':')[0]
# start_min = timeStr[0].rstrip().split(':')[1]
# end_hour = timeStr[1].rstrip().split(':')[0]
# end_min = timeStr[1].rstrip().split(':')[1]

# start_date = datetime.date.today()
# end_date = datetime.date.today()
# start_date = datetime.datetime(start_date.year, start_date.month, start_date.day, int(start_hour), int(start_min), 0)
# end_date = datetime.datetime(end_date.year, end_date.month, end_date.day, int(end_hour), int(end_min), 0)
# total_difference = ( end_date - start_date)
# total_delta = total_difference.total_seconds()
# print ((total_delta/60/60))

# hours = (total_delta/60/60)
# minutes = ((total_delta/60) % 60)
# print(hours)
# print(minutes)

# language = [str(i.text).strip() for i in soup.find_all(class_='gallerypreview pgroup-0')]
# print(language)