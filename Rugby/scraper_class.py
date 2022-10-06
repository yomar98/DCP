from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def load_and_accept_cookies()-> webdriver.Chrome:
    driver = webdriver.Chrome()
    url = 'https://www.prodirectrugby.com/'
    driver.get(url)
    delay = 5
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gdpr-consent-notice"]')))
        print("Frame Ready!")
        driver.switch_to.frame('gdpr-consent-notice')
        accept_cookies_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="save"]')))
        print("Accept Cookies Button Ready!")
        accept_cookies_button.click()
        time.sleep(1)
    except TimeoutException:
        print("Loading took too much time!")

    return driver 


class Scraper:
    def __init__(self, url: str = 'https://www.prodirectrugby.com/' ):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)

    def click_element (self, xpath = str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click
        '''finds element to click - made cleaner by choosing the element as opposed to step by step'''

    def accept_cookies(self, xpath: str = '//button[@id="truste-consent-button"]'):
        self.click_element(xpath)
        '''Specifally to accept cookies- click element renamed for clarity'''
    
    def find_elements_in_container (self,
                                    xpath_container: str,
                                    tag_elements:str)-> list:
        container = self.driver.find_element(By.XPATH, xpath_container)
        elements_in_container = container.find_elements(By.XPATH, f'./{tag_elements}')
        return elements_in_container