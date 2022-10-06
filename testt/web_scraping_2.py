from wsgiref import headers
import requests 
from bs4 import BeautifulSoup

baseurl = 'https://www.prodirectrugby.com/'

bootslinks = []
print
for x in range (1,28):
    r = requests.get('https://www.prodirectrugby.com/lists/mens-rugby-boots.aspx?qfhr=cleats&p=2') 
    print()
    html=r.text
    soup = BeautifulSoup(r.content, 'html.parser')
    bootslist = soup.find_all('div', class_='item')
    for item in bootslist:
        for link in item.find_all('a', href=True):
            bootslinks.append(baseurl + link['href'])
        

#testlink = 'https://www.prodirectrugby.com/products/adidas-Rugby-Adizero-RS7-FG-Silver-White-Grey-Mens-Boots-260439.aspx'
 

for link in bootslinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    name = soup.find('h1', class_='product-name__colourway').text.strip()
    description = soup.find('div', class_='right-column').text.strip()
    price = soup.find('p', class_='price').text.strip()
    countrysize = soup.find('ul', class_='size-country').text.strip()
    wearsize = soup.find('div', class_='selector fixedWidth').text.strip()
    boots = {
        'name': name, 
        'description': description,
        'price': price,
        'countrysize': countrysize,
        'wearsize': wearsize,
    }

    print(boots)
