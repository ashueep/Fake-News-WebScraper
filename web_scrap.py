from bs4 import BeautifulSoup
import requests
import lxml
import json

HEADERS = []
URLS = []

js_list = list()

def Scrapper(page):
    
    url = 'https://timesofindia.indiatimes.com/times-fact-check/'
    if page != 1 : url += str(page)
    print(url)
    # print(url)
    content = requests.get(url)

    if str(content) is '<Response [404]>':
        return 0

    soup = BeautifulSoup(content.text, "html.parser")
    l = soup.find_all('span',class_ = 'w_tle')

    urls = list()

    for texts in l:
        js_list.append({
            "Header" : texts.text,
            "Url" : "https://timesofindia.indiatimes.com/"  + texts.a['href']
        })
    
    # js['Headers'] = HEADERS
    # js_dict['Urls'] = URLS
    with open ("Test2.json","w") as file:
        json.dump(js_list,file)

def main():
    for page in range(15):
        Scrapper(page+1)
    
    print(len(js_list))

if __name__ == '__main__':
    main()