
import requests
import json
from bs4 import BeautifulSoup


dictionary = {}

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser')
all = []
for headline in obj.find_all('div',class_='teaser_conten1'):
    x = json.dumps(headline.find('h1').text)
    y = json.dumps(headline.find('h2').text)
    z = json.dumps(headline.find('div', class_='date').text)
    dictionary['Kategori']=x
    dictionary['Judul']=y
    dictionary['Waktu']=z    
    
    all.append( dict(dictionary))    
    

dict_web = all
with open('scrap.json', 'w') as file:
    json.dump(dict_web, file, indent=4)

    '''Dibantu oleh Azhar dan Pak Lukmanul H.'''
