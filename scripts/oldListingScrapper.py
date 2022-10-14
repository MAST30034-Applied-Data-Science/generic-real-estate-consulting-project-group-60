'''
Get all the postcode in VIC
'''
import pandas as pd
# Defining of the dataframe
# built-in imports
import re
from json import dump

from collections import defaultdict

# user packages
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import requests
df = pd.DataFrame(columns=['postcode'])
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
table = BeautifulSoup(requests.get('https://www.worldpostalcodes.org/l1/en/au/australia/list/r1/list-of-postcodes-in-victoria',headers = headers).text, "html.parser")
# Collecting Ddata
for row in table.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        postcode = columns[0].text.strip()

        df = df.append({'postcode':postcode}, ignore_index=True)    
postcodes = df['postcode'].tolist()
postcodes = [int(x) for x in postcodes if x]

url_links = {}



postcode_list = postcodes # All the postcode in the Victoria

# begin code
# generate list of urls to visit
for postcode in postcode_list[674:]:
    search_postcode = f"https://www.oldlistings.com.au/search/postcode?id={postcode}&type=rent"
    bs_object = BeautifulSoup(requests.get(search_postcode,headers = headers).text, "html.parser")
    if bs_object.find("p", {"class": "sub-page-h1"}).text == "Suburb Not Found":
        continue
    else:
        if bs_object.find("p",{"class":"sub-page-h1"}).text != "Postcode Search":
            url_links[search_postcode] = postcode
        else:
            for url in bs_object.find("section",{"class":"page-wrap grid-container"}) \
                                .find("section",{"class":"grid-100"}) \
                                .findAll("a"):
                url_links["https://www.oldlistings.com.au"+url["href"]] = postcode

'''
# funtion aims to change current ip to avoid forbidden
def changeIP(current_ip):
    url = "https://free-proxy-list.net/"
    headers = {'User-Agent':random.choice(user_agents)} 
    bs_object = BeautifulSoup(requests.get(url,headers = headers).text, "html.parser") 
    for tr in bs_object.find("tbody").findAll("tr"):
        ip_information = tr.findAll("td")
        proxy = ip_information[0].text + ":" + ip_information[1].text
        if ip_information[4].text == "elite proxy" and proxy != current_ip:
            break
    return proxy
'''

# for each url, scrape some basic metadata
'''
iterate through all the links in the list 
'''

from collections import defaultdict

property_metadata = defaultdict(dict)
#current_ip = changeIP(local_ip)
for row,index in url_links.iterrows():
    # sleep for 0-1 seconds
    time.sleep(random.random())
    
    headers = {'User-Agent':random.choice(user_agents)}  
    
    # if 403 happened, changed current ip address 
    bs_object = BeautifulSoup(requests.get(row["links"],headers = headers).text, "html.parser") 
    '''
    if bs_object.find("head").find("title").text == "403 Forbidden":
        current_ip = changeIP(current_ip)
       bs_object = BeautifulSoup(requests.get(row["links"],headers = headers, proxies={"http": current_ip, "https": current_ip}).text, "html.parser")
    '''    
        
    postcodes = row["postcode"]
    bs_element = []
    if bs_object.find_all('div', {'class':'property odd clearfix'}) is not None: 
        bs_element.append(bs_object.find_all('div', {'class':'property odd clearfix'}))
    
    if bs_object.find_all('div', {'class':'property even clearfix'}) is not None:
        bs_element.append(bs_object.find_all('div', {'class':'property even clearfix'}))
    
    if len(bs_element) > 0:    
        for bs in bs_element:     
            for prop in bs:
                # looks for the header class to get property name
                name = prop \
                    .find("h2", {"class": "address"}) \
                    .text
                property_metadata[name]['name'] = prop \
                    .find("h2", {"class": "address"}) \
                    .text
                property_metadata[name]['postcode'] = postcodes

                cost = []     
                for li in prop.find("section", {"class": "grid-100 historical-price"}).find("ul"):              
                    cost_text = li.text
                    cost.append(cost_text)
                if " " in cost:
                    cost.remove(" ")
                property_metadata[name]['cost_text'] = cost

                if prop.find("p",{"class":"property-meta type"}) is not None:
                    property_metadata[name]['property_type'] = prop.find("p",{"class":"property-meta type"}).text

                if prop.find("p",{"class":"property-meta bed"}) is not None:
                    property_metadata[name]['bed'] = prop.find("p",{"class":"property-meta bed"}).text

                if prop.find("p",{"class":"property-meta bath"}) is not None:
                    property_metadata[name]['bath'] = prop.find("p",{"class":"property-meta bath"}).text

                if prop.find("p",{"class":"property-meta car"}) is not None:
                    property_metadata[name]['car'] = prop.find("p",{"class":"property-meta car"}).text

                property_metadata[name]['latitude'] = prop["data-lat"]  
                property_metadata[name]['longitude'] = prop["data-lng"]

# output to example json in data/Property/
# Since the ip address are frequently forbidded by the old listing 
# so the final output might not reflect the full data of history data
# the final version of history data were aggregated from the other output of this notebook from each team member

pd.DataFrame(property_metadata).to_csv("../data/Property/history_data.csv")