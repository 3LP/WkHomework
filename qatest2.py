#   
#   
#   
#
#
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#
# Classes
#
input_url = None

class UIbugsearch(unittest.TestCase):

    def setUp(self):
        cline_input = input("Enter Web App Url: ")
        global input_url
        input_url = 'http://' + cline_input 
        self.driver = webdriver.Firefox()

    def test_hover(self):
        # SCRAPE AND TEST
        driver = self.driver
        driver.get(input_url)
        element = driver.find_elements_by_css_selector(".video-thumb")
        for x in element:
            mouse_over = ActionChains(driver).move_to_element(x)
            # mouse_over.perform()

        
    def tearDown(self):
        self.driver.close()
#
#
#
if __name__ == "__main__":
    unittest.main()