import json
from select import select
from unicodedata import name
from urllib import request
from warnings import filters 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib
import os  

class Scraper: 
    def __init__(self, url: str = 'https://www.prodirectsport.com/rugby/' ):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        time.sleep(3)
        
    def search_boots(self):
        search = self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div/div[1]/div[2]/input') # finding search bar 
        search.send_keys('boots') # inputting boots into search bar 
        search.send_keys(Keys.RETURN) # hitting the search button 
        time.sleep(3)
    
    def open_all_boots_page(self):
        all_boots = self.driver.find_element(by=By.XPATH, value='/html/body/main/section[2]/section/div[2]/ul/li[1]/div/ul/li[1]/a')
        boots_link = all_boots.get_attribute('href')
        self.driver.get(boots_link)

    def get_boots_links(self):
        container = self.driver.find_element_by_xpath('/html/body/main/section[2]/section/div[3]/div[1]')
        boots_list = container.find_elements_by_xpath('//div[contains(@class, "lister-grid__item")]')
        links = []
        for boots in boots_list:
            a_tag = boots.find_element_by_tag_name('a')
            boots_link = a_tag.get_attribute('href')
            links.append(boots_link)

        return links

    def next_page(self):
        container = self.driver.find_element_by_xpath('/html/body/main/section[2]/section/div[3]/div[1]')
        next_page_button = container.find_element(by=By.XPATH, value='//a[contains(@class, "pagination__next")]')
        next_page_link = next_page_button.get_attribute('href')
        self.driver.get(next_page_link)
    
    def get_all_links(self):
        all_links = []
        all_links.extend(self.get_boots_links())
        for x in range(0, 34):
            self.next_page()
            all_links.extend(self.get_boots_links())
        
        return all_links
    
class Data_handling(Scraper):
    def __init__(self, url: str = 'https://www.prodirectsport.com/rugby/'):
        super().__init__(url)
        self.search_boots()
        self.open_all_boots_page()
        self.get_boots_links()
        self.get_all_links()

    def description_of_boots(self):
        container = self.driver.find_element_by_xpath('/html/body/main/section[2]/section/div[3]/div[1]')
        boots_details = container.find_element(by=By.XPATH, value='/html/body/main/div[1]/div[1]') # name, colour, price xpath
        name = boots_details.find_element_by_class_name('ml-meta__title')
        colour = boots_details.find_element_by_class_name('ml-meta__colourway')
        price = boots_details.find_element_by_class_name('ml-meta__prices ml-prices')

        print(name, colour, price)

if __name__ == '__main__':
    prodirect_rugby = Data_handling()
    prodirect_rugby.description_of_boots()
