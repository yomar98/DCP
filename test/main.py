from lib2to3.pgen2 import driver
from scraper import Scraper #from the previous file we made
import time #so we actually se the page

if __name__ == '__main__':
    bot = Scraper() #calls scraper
    time.sleep(8) #8 second delay before webpage closes

    accept_cookies = self.driver.find_element(By.XPATH, '<xpath button for consent/other>')
accept_cookies.click()

driver.switch_to_frame('<frame id>') # This is the id of the frame - don't include 'id'
    accept_cookies_button = driver.find_element(by=By.XPATH, value='<path>')
    accept_cookies_button.click()
