from ast import Div
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/Users/Aicore/Desktop/chromedriver"

driver = webdriver.Chrome(PATH)
url = 'https://www.prodirectrugby.com/'
driver.get(url)

driver.find_element_by_id('cookie')
driver.find_element_by_xpath('//*[@id="hide-cookie-message"]').click()  # closing cookies before proceeding 

driver.implicitly_wait(2)

search = driver.find_element_by_id('siteSearchInput')  #searching for the boots in the search bar
search.send_keys("boots")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(2)

boot_details = driver.find_element_by_class_name('leftbar ') # go to left hand side of screen where there the filters are located 
boot_details = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/a').click() # reset filter options

driver.implicitly_wait(2)

boot_details = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]') # filters tab -- automatically opens up brands tab. No need for code 

boot_details = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div[1]').click() # click canterbury brands tab 

driver.implicitly_wait(2)



driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scrolling to end of page 
time.sleep(5)

boots_brand_list = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div[1]/div/ul')
boots_brand_list = [ul.get_attribute('href') for ul in list]
print(boots_brand_list)



# try:
#     boot_brands = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'holder'))
#     )
#     boots_brand_list = boot_brands.find_element_by_class_name('matches')
#     print(boots_brand_list.text)
# finally:
#     driver.quit()



# try:                                                            #contents of whole main page
#     main_boots_page = WebDriverWait(driver, 10).until(                #wait 10 seconds before running this part of code to give CPU a chance to get to new url
#         EC.presence_of_element_located((By.ID, "content"))      
#     )
#     boots = main_boots_page.find_elements_by_class_name('item')       # found specifically details of boots using class tag 
#     for boot in boots:
#         boots_details = boot.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[4]') # finding xpath of all boots in one part of xpath code
#         print(boots_details.text)

# except:                                                         # if not found then quit
#     driver.quit()

# driver.quit()




# def get_canterbury_boots(self, boot_brand):
#     query = f"https://www.prodirectrugby.com/lists/mens-rugby-boots.aspx?qfhr=cleats{boot_brand}".replace(' ', '+')
#     print(query)




# for canterbury_details in boot_details:
#     boot_details = canterbury_details.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div[1]/div/ul/li[1]/a').click() # adidas specific 
#     try: 
#         canterbury_boots_page = WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.ID, "content"))
#         )
#         canterbury_boots = canterbury_boots_page.find_element_by_class_name('item')
#         for canterbury_boot in canterbury_boots:
#             canterbury_boot_details = canterbury_boot.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[4]')
#             print(canterbury_boot_details).text
#     except:
#         driver.quit()






try:                                                            #contents of whole main page
    main_boots_page = WebDriverWait(driver, 10).until(                #wait 10 seconds before running this part of code to give CPU a chance to get to new url
        EC.presence_of_element_located((By.ID, "content"))      
    )
    boots = main_boots_page.find_elements_by_class_name('item')       # found specifically details of boots using class tag 
    for boot in boots:
        boots_details = boot.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[4]') # finding xpath of all boots in one part of xpath code
        print(boots_details.text)

except:                                                         # if not found then quit
    driver.quit()

driver.quit()

