import time 
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/Users/Aicore/Desktop/chromedriver')

driver.get('https://www.rottentomatoes.com/browse/dvd-streaming-all');

for n in range (8):
    driver.find_element_by_css_selector('.btn.ntn-secondary-rt.mb-load-btn').click()
    s = randint(1, 10)
    time.sleep(s)

page = driver.page_source

soup = BeautifulSoup(page, "html.parser")
title_list = soup.find_all("h3", class_="movieTitle")
for title in title_list:
    print(title.get_text())

print("There are " + str(len(title_list)) + " movies in the list.")

driver.quit()
