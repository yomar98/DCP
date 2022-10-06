import time 
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup
import requests

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
 
boots = soup.find(name='a', attrs={'class': 'navigation', 'role': 'navigation', 'class': 'inner', 'id': 'primary-nav', 'class': 'inner'})
print(boots)




driver = webdriver.Chrome('/Users/Aicore/Desktop/chromedriver/')
url = 'https://www.prodirectrugby.com/'
driver.get(url)
time.sleep(5)
#try:
 #   driver.switch_to_frame('/information/privacy-policy.asp#cookies')
  #  accept_cookies_button = driver.find_element_by_xpath('//*[@href=accept')
   # accept_cookies_button.click()




# for n in range (10):
#     driver.find_element_by_css_selector('.btn.ntn-secondary-rt.mb-load-btn').click()
#     s = randint(1, 10)
#     time.sleep(s)

# page = driver.page_source

# soup = BeautifulSoup(page, "html.parser")
# title_list = soup.find_all("h3", class_="rugbyBoots")
# for title in title_list:
#     print(title.get_text())

# print("There are " + str(len(title_list)) + "rugby boots in the page.")

# driver.quit() 


#from scraper import Scraper #from the previous file we made

#if __name__ == '__main__':
 #   bot = Scraper() #calls scraper
  #  time.sleep(8) #8 second delay before webpage closes

