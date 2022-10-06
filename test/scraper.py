from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class Scraper:
    def __init__(self, url: str = 'https://www.prodirectrugby.com/'):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

    def click_element (self, xpath = str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click
    
    def accept_cookies(self, xpath: str = '//button[@id="truste-consent-button"]'):
        self.click_element(xpath)
        '''Specifally to accept cookies- click element renamed for clarity'''
    
    def find_elements_in_container (self,
                                    xpath_container: str,
                                    tag_elements:str)-> list:
        container = self.driver.find_element(By.XPATH, xpath_container)
        elements_in_container = container.find_elements(By.XPATH, f'./{tag_elements}')
        return elements_in_container


class ProDirectScraper (Scraper):
    def search_boot(self,
                    size,
                    brand,
                    xpath_search_bar: str = '//input[@class="search-tect"]'):
        self.accept_cookies()
        time.sleep(2)
        search_bar = self.driver.find_element(By.XPATH, xpath_search_bar)
        search_bar.click()
        time.sleep(1)
        search_bar.send_keys(boot)
        time.sleep(1)
        self.click_element('//[class="search-submit"]')
