from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()


url = 'https://www.prodirectrugby.com/'

driver.get(url)

try: 
        driver.switch_to_frame('cookie')
        close_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]')
        close_cookies_button.click()
        time.sleep(3)
        driver.switch_to_default_content()

# except:

# driver.switch_to_frame('cookie')
# close_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="hide-cookie-message"]')
# close_cookies_button.click()


# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//*[@id="page"]')
# driver.find_element_by_xpath('//*[@id="cookie"]')
# driver.find_element_by_xpath('//*[@id="hide-cookie-message"]').click

