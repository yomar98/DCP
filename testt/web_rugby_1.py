import time 
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup
import requests
import testt.web_scraping_2 as web_scraping_2

driver = webdriver.Chrome('/Users/Aicore/Desktop/chromedriver/')
driver.get('https://www.prodirectrugby.com/');

page = requests.get('https://www.prodirectrugby.com/')
html = page.text
soup = BeautifulSoup(html, 'html.parser')
select_tag = soup.find("Boots")
options = select_tag.find_all("VIEW ALL ADULT RUGBY BOOTS")
for option in options:
    print(option.text)


r = requests.get('https://www.prodirectrugby.com/')
html_string = r.text


driver = webdriver.Chrome('/Users/Aicore/Desktop/chromedriver/')
url = 'https://www.prodirectrugby.com/'
driver.get(url)
time.sleep(5)

if __name__ == '__main__':
    bot = web_scraping_2() #calls scraper
    time.sleep(8) #8 second delay before webpage closes
