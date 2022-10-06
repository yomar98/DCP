from tkinter.tix import Tree
import unittest
from selenium import webdriver
import page
from youtube_test.page import MainPage

class PythonOrdSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/Aicore/Desktop/chromedriver")
        self.driver.get('https://www.python.org')

    def test_search_python(self):
        MainPage = page.MainPage(self.driver)
        assert MainPage.is_title_matches()
        MainPage.search_text_element = "pycon"
        MainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()