# 
#   
#   
#   Tests Website UI
#
#
import os,sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
#
# Classes and Global Variables
#
input_url = None

class UIbugsearch(unittest.TestCase):

    def setUp(self):
        cline_input = input("Enter Web App Url: ")
        global input_url
        input_url = 'http://' + cline_input 
        self.driver = webdriver.Chrome()
    #
    # Create a List of Every Link and Click on It
    #
    def test_links(self):
        driver = self.driver
        driver.get(input_url)
        links = driver.find_elements_by_tag_name('a')
        link_urls = [link.get_attribute('href') for link in links]
        for url in link_urls:
            driver.get(url)

        
    def tearDown(self):
        self.driver.close()
#
#
#
if __name__ == "__main__":

    unittest.main()