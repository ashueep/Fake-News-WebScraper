from bs4 import BeautifulSoup
import requests
import lxml
import json
import re

final_list = []

def Scrapping(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    try:
        str = soup.find('div','ga-headlines').text
        pattern = re.compile(r'CLAIM.*TRUTH')
        match = pattern.search(string = str)

        return match.group()[5:match.span()[1] - 6]
    except:
        print(url + " is causing error/or showing None")

    # return match.group()[5:match.span()[1] - 6]


loaded_json = json.load(open('Test.json','r'))

# for urls in loaded_json:
#     url = urls['Urls']

for url in loaded_json:
    d = {
        'Header' : url['Header'],
        'Body' : Scrapping(url['Url'])
    }
    final_list.append(d)

    print(d)


with open('Final.json','w') as file:
    json.dump(final_list, file)
 
