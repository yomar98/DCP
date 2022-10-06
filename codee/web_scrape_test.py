from ast import Div
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import itertools
import urllib

import time

PATH = "/Users/Aicore/Desktop/chromedriver"

driver = webdriver.Chrome(PATH)
url = 'https://www.prodirectrugby.com/'
driver.get(url)

search = driver.find_element_by_id('siteSearchInput')           #searching for the boots in the search bar
search.send_keys("boots")
search.send_keys(Keys.RETURN)

class Scraper_boot_details:
    try: 
        boots_brand = WebDriverWait(driver, 10).until(                #wait 10 seconds before running this part of code to give CPU a chance to get to new url
            EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div[3]/div[2]/div[1]/div"))
        )
        boots_brand = boots_brand.find_elements_by_class_name('holder')       # found specifically details of boots using class tag 
        for boot_brand in boots_brand:
            boots_brand_details = boots_brand.find_element_by_class_name('matches') # finding xpath of adidas boots in one part of xpath code
            print(boots_brand_details.text)

    except:                                                         # if not found then quit
        driver.quit()


# def get_all_boots(self, boot_brand):
#     query = f"https://www.prodirectrugby.com/lists/mens-rugby-boots.aspx?qfhr=cleats{boot_brand}".replace(' ', '+')
#     print(query)





# class AllBootsScraper(Bot):
#     def __init__(self):
#         super().__init__()

#         boot_brand = [
            
  
#         ]
#         boot_sub_type = [
           
#         ]
#         boot_ground_type = [

#         ]
#         boot_collection = [


#         ]
#         boot_model = [

#         ]
#         boot_class = [

#         ]
#         boot_flavour = [

#         ]
#         boot_sustainable = [

#         ]
#         boot_sizes = [

#         ]
#         boot_base_colour = [

#         ]
#         boot_price_range = [ 

#         ]




# link = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div[1]/div/ul/li[1]/a') # link to specifically adidas boots
# link.click()

# class Scraper:
#     try:                                                            #contents of whole main page
#         adidas_boots_page = WebDriverWait(driver, 10).until(                #wait 10 seconds before running this part of code to give CPU a chance to get to new url
#             EC.presence_of_element_located((By.ID, "content"))      
#         )
#         adidas_boots = adidas_boots_page.find_elements_by_class_name('item')       # found specifically details of boots using class tag 
#         for adidas_boot in adidas_boots:
#             adidas_boots_details = adidas_boot.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[4]') # finding xpath of adidas boots in one part of xpath code
#             print(adidas_boots_details.text)

#     except:                                                         # if not found then quit
#         driver.quit()

# # driver.back()

# # link = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div[1]/div/ul/li[8]/a') # link to specifically nike boots
# # link.click()

# # try:                                                            #contents of whole main page
# #     nike_boots_page = WebDriverWait(driver, 10).until(                #wait 10 seconds before running this part of code to give CPU a chance to get to new url
# #         EC.presence_of_element_located((By.ID, "content"))      
# #     )
# #     nike_boots = nike_boots_page.find_elements_by_class_name('item')       # found specifically details of boots using class tag 
# #     for nike_boot in nike_boots:
# #         nike_boots_details = nike_boot.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[4]') # finding xpath of nike boots in one part of xpath code
# #         print(nike_boots_details.text)

# # except:                                                         # if not found then quit
# #     driver.quit()


# #driver.quit()

