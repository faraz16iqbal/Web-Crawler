#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[48]:


import urllib.request

html = urllib.request.urlopen("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/").read()

soap = BeautifulSoup(html, 'html.parser')

all = soap.find_all("div", {"class" : "propertyRow"})
address = soap.find_all("span", {"class" : "propAddressCollapse"})
# all[0].find("h4", {"class": "propPrice"}).text.replace("\n", "").strip()

import urllib.request
soap = BeautifulSoup(html, 'html.parser')
base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
l=[]
for page in (0,10,20):
    html = urllib.request.urlopen(base_url + str(page) + '.html').read()
    print(base_url + str(page) + '.html')
    all = soap.find_all("div", {"class" : "propertyRow"})
    for item in all:
        d={}
        try:
            d['Address'] = (item.find_all("span", {"class" : "propAddressCollapse"})[0].text)
        except:
            d['Address'] = None
        try:
            d['Locality'] = (item.find_all("span", {"class" : "propAddressCollapse"})[1].text)
        except:
            d['Locality'] = None
        d["Price"] = (item.find("h4", {"class": "propPrice"}).text.replace("\n", "").strip())
        try:
            d['Beds'] = (item.find("span", {"class" : "infoBed"}).find("b").text)
        except:
            d['Beds'] = (None)
        try:
            d['Area'] = (item.find("span", {"class" : "infoSqFt"}).find("b").text)
        except:
            d['Beds'] = (None)
        try:
            d['Full Baths'] = (item.find("span", {"class" : "infoValueFullBath"}).find("b").text)
        except:
            d['Full Baths'] = (None)
        try:
            d['Half Baths'] = (item.find("span", {"class" : "infovalueHalfBath"}).find("b").text)
        except:
            d['Half Baths'] = (None)
        for column_group in item.find_all("div", {"class" : "columnGroup" }):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class" : "featureGroup"}), column_group.find_all("span", {"class" : "featureGroup"})):
                if("Lot Size") in feature_group.text:
                    d['Lot Size'] = ("1.5-2 Acres")
        l.append(d)


# In[61]:


print(l)


# In[62]:


import pandas
df=pandas.DataFrame(l)
(df)


# #### df.to_csv("Output.csv")
