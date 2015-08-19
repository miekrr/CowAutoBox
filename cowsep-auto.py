import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

TWITCH_USER = "user"
TWITCH_PASS = "pass"
COWSEP_WEBSITE = "http://www.cowsep.com"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def open_boxes(self):
        driver = self.driver
        item_name = "bullbox"
        while True:
            elem = driver.find_element_by_name("csrf-token")
            csrf_token = elem.get_attribute("content")
            link = COWSEP_WEBSITE + "/crates.php?crate=" + item_name + "&csrf_token=" + csrf_token
            print(link)
            driver.get(link)
            body = driver.find_element_by_xpath("/html/body/")
            time.sleep(2)
            driver.get("http://www.cowsep.com")
            #driver.refresh()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(COWSEP_WEBSITE)
        #self.assertIn("Python", driver.title)

        login_link = driver.find_element_by_css_selector("a[href='login.php']")
        login_link.click()
        time.sleep(3)
        login_box = driver.find_element_by_name("login")
        login_box.send_keys(TWITCH_USER)

        pass_box = driver.find_element_by_name("password")
        pass_box.send_keys(TWITCH_PASS)
        pass_box.send_keys(Keys.RETURN)

        time.sleep(2)
        self.open_boxes()

        #assert "No results found." not in driver.page_source


    def tearDown(self):
        #self.driver.close()
        print("bye!")

if __name__ == "__main__":
    unittest.main()
