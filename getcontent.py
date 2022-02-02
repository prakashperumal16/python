from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
from selenium import webdriver
import json

# Opening JSON file
f = open('json_template.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
print(data)
# exit(0)
# data = {}
# data['key'] = 'value'
# data['city'] = ''
# data['website'] = ''
# data['companyName'] = ''
# data['firstName'] = ''
# data['lastName'] = ''
# data['category'] = ''
# data['zipcode'] = ''
# data['email'] = ''
# data['country'] = ''
# data['contactNumber'] = ''
# data['address'] = ''
# data['companyDescription'] = ''
# data['status'] = ''


dr = webdriver.Chrome(executable_path=r'C:\Users\Prakash Perumal\AppData\Local\chromedriver.exe')
dr.get("https://themakery.de/schnittkaese-im-feierabend/Berlin")
soup = bs(dr.page_source,"lxml")



storeName = [str(i.text).strip() for i in soup.find_all(class_='relatetitle txt_large pad-l-bottom')]
data['storeName']=storeName[0]
service_name = [str(i.text).strip() for i in soup.find_all(class_='title_small medium pad-l-bottom')]
data['eventName']=service_name[0]

service_price = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='subtitle txt_medium min marg-xxs-bottom')]
data['priceWithoutVat']=service_price[0]
data['pricePerPerson']=service_price[0]
Service_description  = [str(i.text).strip() for i in soup.find_all(class_='readmore')]
data['description']=Service_description[0]

service_image = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='gallerypreview pgroup-0')]
data['service_image']=service_image[0]

what_is_included  = [str(i.text).strip() for i in soup.find_all(class_='serviceitem')]
data['headers']['What Is Included']['value']=what_is_included[0]

requirement = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='subtitle txt_medium min marg-xxs-bottom')]
data['headers']['requirement']['value']=requirement[0]

good_to_know  =[str(i.text).strip() for i in soup.find_all(class_='serviceitem')]
data['good_to_know']=good_to_know[2]

language = [str(i.text).strip() for i in soup.find_all(class_='subtitle txt_medium min')]

data['specifications']['language']=language[3]
json_data = json.dumps(data)
print(json_data)

