from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import random
from selenium import webdriver
import json
import sys

if len(sys.argv) <= 1:
    print("Please pass a valid link")
    exit(1)

url = sys.argv[1]
 
# Opening JSON file
f = open('json_template.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

#collect the html data


dr = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
dr.get(url)
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
data['coverimage']=service_image[0]

what_is_included  = [str(i.text).strip() for i in soup.find_all(class_='serviceitem')]
data['headers']['What Is Included']['value']=what_is_included[0]

requirement = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='subtitle txt_medium min marg-xxs-bottom')]
data['headers']['Requirements']['value']=requirement[0]

store_description = [str(i.text) for i in soup.find_all(class_='fulltext')]
data['description']=store_description[1]

data_image = soup.find_all(class_='gallerypreview pgroup-0')
image_tag=re.findall(r"'(.*?)'", data_image[0]["style"], re.DOTALL)
data["images"] =  image_tag
data["storeImage"] =  image_tag

language = [str(i.text).strip() for i in soup.find_all(class_='subtitle txt_medium min')]

data['specifications']['language']=language[3]
json_data = json.dumps(data)

outfilename = str(service_name[0])+'_'+str(storeName[0]) +'_service.json'

with open(outfilename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
