import pandas as pd
import re
from json import dump
from collections import defaultdict
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import requests

'''
This part is about to scrape the All postcode in VIC through web scrapping
'''
df = pd.DataFrame(columns=['postcode'])
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

# We get the full postcode list in VIC in this website:
# https://www.worldpostalcodes.org/l1/en/au/australia/list/r1/list-of-postcodes-in-victoria

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

'''
This part is about to get the link of all rental property in victoria in each postcode
And all the link would be store in url_links
'''

BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 31)  # we scrape not more than 31 pages in each postcode
postcode_list = postcodes # All the postcode in the Victoria

# begin code
url_links = []
property_metadata = defaultdict(dict)
# generate list of urls to visit
for postcode in postcode_list:
    postcode_url = BASE_URL + f"/rent/?excludedeposittaken=1&sort=default-desc&postcode={postcode}&page="
    for page in N_PAGES:
        url = postcode_url + f"{page}"
        # find the unordered list (ul) elements which are the results, then
        # find all href (a) tags that are from the base_url website.
        bs_object = BeautifulSoup(requests.get(url,headers = headers).text, "html.parser")
        if bs_object.find("div", {"class": "css-18vn4hf"}) is not None:
        # if this page reachs the limit, then break
            break
        else:
            if bs_object.find("ul",{"data-testid": "results"}) is not None:
                # if this page contains the property url then record the url
                index_links = bs_object \
                    .find(
                        "ul",
                        {"data-testid": "results"}
                    ) \
                    .findAll(
                        "a",
                        href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
                    )
                for link in index_links:
                    # if its a property address, add it to the list
                    if 'address' in link['class']:
                        url_links.append(link['href'])
'''
This part is to find the feature of the property which storing in our url list
'''

# for each url, scrape some basic metadata
for property_url in url_links[1:]:
    bs_object = BeautifulSoup(requests.get(property_url,headers = headers).text, "html.parser")
    
    if bs_object.find("h1", {"class": "css-164r41r"}) is not None:
        # looks for the header class to get property name
        property_metadata[property_url]['name'] = bs_object \
            .find("h1", {"class": "css-164r41r"}) \
            .text

    
        # looks for the div containing a summary title for cost
        property_metadata[property_url]['cost_text'] = bs_object \
            .find("div", {"data-testid": "listing-details__summary-title"}) \
            .text
    
        property_metadata[property_url]['property_type'] = bs_object \
                .find("div", {"data-testid": "listing-summary-property-type"}) \
                .text
        '''
        The function used to find the agent name of the property, use according to individual needs
        property_metadata[property_url]['agent'] = [
        feature.text for feature in bs_object \
            .find("div", {"data-testid": "listing-details__residential-header-agent-copy"}) \
            .findAll("a")]
        '''
        
        for li_tag in bs_object.find_all('ul', {'data-testid':'listing-summary-strip'}):
            value=[]
            for span_tag in li_tag.find_all('li'):           
                value.append(span_tag.find('strong').text)
                property_metadata[property_url]['property_feature'] = value
    
    
        # extract coordinates from the hyperlink provided
        # i'll let you figure out what this does :P
        property_metadata[property_url]['coordinates'] = [
            float(coord) for coord in re.findall(
                r'destination=([-\s,\d\.]+)', # use regex101.com here if you need to
                bs_object \
                    .find(
                        "a",
                        {"target": "_blank", 'rel': "noopener noreferer"}
                    ) \
                    .attrs['href']
            )[0].split(',')
        ]
        property_metadata[property_url]['rooms'] = [
            re.findall(r'\d\s[A-Za-z]+', feature.text) for feature in bs_object \
                .find("div", {"data-testid": "property-features"}) \
                .findAll("span", {"data-testid": "property-features-text-container"})
        ]
    
    
        property_metadata[property_url]['desc'] = re \
            .sub(r'<br\/>', '\n', str(bs_object.find("p"))) \
            .strip('</p>')
    

# output to example json in data/raw/

with open('../data/Property/15000_property.json', 'w') as f:
    dump(property_metadata, f)