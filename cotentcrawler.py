import datetime
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import random
from selenium import webdriver
import json
import os
import re

def get_hours_min(timestr):
    
    start_hour = timestr[0].rstrip().split(':')[0]
    start_min = timestr[0].rstrip().split(':')[1]
    end_hour = timestr[1].rstrip().split(':')[0]
    end_min = timestr[1].rstrip().split(':')[1]

    start_date = datetime.date.today()
    end_date = datetime.date.today()
    start_date = datetime.datetime(start_date.year, start_date.month, start_date.day, int(start_hour), int(start_min), 0)
    end_date = datetime.datetime(end_date.year, end_date.month, end_date.day, int(end_hour), int(end_min), 0)
    total_difference = ( end_date - start_date)
    total_delta = total_difference.total_seconds()
    print ((total_delta/60/60))

    hours = (total_delta/60/60)
    minutes = ((total_delta/60) % 60)
    return hours,minutes

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
    
    
    data[0]['legalBusinessName']=url
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
    if (len(service_image) > 0):
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
    image_tag=[]
    for image in data_image:
        image_tag.append(re.findall(r"'(.*?)'", image["style"], re.DOTALL)[0])
    if len(image_tag) > 0:
        data[0]["images"] =  image_tag
        data[0]["storeImage"] =  image_tag[0]
        data[0]["coverimage"] =  image_tag[0]
        
    print('here 1')
    # language = [str(i.text).strip() for i in soup.find_all(class_='subtitle txt_medium min')]
    if 'Sprache' in titles :
        data[0]['specifications']['language']=subTitles[titles.index('Sprache')]
    print('here 2')
    

    if 'Uhrzeit' in titles :
        timestr = subTitles[titles.index('Uhrzeit')]
        if timestr:
            service_hours, service_min = get_hours_min(timestr.split('-'))
            data[0]['serviceDuration']['hours'] = int(service_hours)
            data[0]['serviceDuration']['minutes'] = int(service_min)

    outfilename = str(service_name[0])+'_'+str(storeName[0]) +'_service.json'
    outfilename=re.sub('[\s+]', '_', outfilename)

    with open(outfilename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


dr = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
dr.get("https://themakery.de/online/kosmetik-und-pflege")
soup = bs(dr.page_source,"lxml")


for a in soup.find_all('a', href=True):
    if str(a['href']).startswith('https://themakery.de') & ('workshops' not in str(a['href'])) & ('privacy' not in str(a['href'])):
        link = a['href']
        # print(link)
        prepare_data(link)

