from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import random
from selenium import webdriver
import json
import os
import re



def prepare_data(url):
     
    # Opening JSON file
    f = open('json_template.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    #collect the html data
    dr.get(url)
    soup = bs(dr.page_source,"lxml")    

    titles = [str(i.text).strip() for i in soup.find_all(class_='title txt_small marg-xxs-bottom')]
    subTitles = [str(i.text).strip() for i in soup.find_all(class_='subtitle txt_medium min')]
    print(titles)
    print()

    storeName = [str(i.text).strip() for i in soup.find_all(class_='relatetitle txt_large pad-l-bottom')]
    data[0]['storeName']=storeName[0]
    service_name = [str(i.text).strip() for i in soup.find_all(class_='title_small medium pad-l-bottom')]
    data[0]['eventName']=service_name[0]

    service_price = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='subtitle txt_medium min marg-xxs-bottom')]
    data[0]['priceWithoutVat']=service_price[0]
    data[0]['pricePerPerson']=service_price[0]
    Service_description  = [str(i.text).strip() for i in soup.find_all(class_='readmore')]
    data[0]['description']=Service_description[0]

    service_image = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='gallerypreview pgroup-0')]
    data[0]['coverimage']=service_image[0]

    what_is_included  = [str(i.text).strip() for i in soup.find_all(class_='serviceitem')]
    data[0]['headers']['What Is Included']['value']=what_is_included[0]

    requirement = [str(i.text).strip().replace("\u20ac","") for i in soup.find_all(class_='subtitle txt_medium min marg-xxs-bottom')]
    data[0]['headers']['Requirements']['value']=requirement[0]

    store_description = [str(i.text) for i in soup.find_all(class_='fulltext')]
    data[0]['storeDescription']=store_description[1]

    host_name = [str(i.text).strip() for i in soup.find_all(class_='txt_medium')]
    data[0]['name']=host_name[len(host_name) -1]

    data_image = soup.find_all(class_='gallerypreview pgroup-0')
    image_tag=re.findall(r"'(.*?)'", data_image[0]["style"], re.DOTALL)
    data[0]["images"] =  image_tag
    data[0]["storeImage"] =  image_tag

    # language = [str(i.text).strip() for i in soup.find_all(class_='subtitle txt_medium min')]

    data[0]['specifications']['language']=subTitles[titles.index('Sprache')]

    outfilename = str(service_name[0])+'_'+str(storeName[0]) +'_service.json'
    outfilename=re.sub('[\s+]', '_', outfilename)

    with open(outfilename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


dr = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
dr.get("https://themakery.de/online/kosmetik-und-pflege")
soup = bs(dr.page_source,"lxml")


for a in soup.find_all('a', href=True):
    if str(a['href']).startswith('https://themakery.de') & str(a['href']).endswith('/Berlin'):
        link = a['href']
        prepare_data(link)




