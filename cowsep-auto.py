import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

TWITCH_USER = "user"
TWITCH_PASS = "pass"
COWSEP_WEBSITE = "http://www.cowsep.com"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.do_twitch_login_for_cowsep()

    def get_status(self, json_data):
        print(json_data)
        data = json.loads(json_data, strict=False)
        if data['status'] != 'fail':
            return True
        return False

    def recycle_item(self, item_id, item):
        link = COWSEP_WEBSITE + "/recycle.php?item=" + item_id + "&item_id=" + item
        print(link)
        self.driver.get(link)
        #return self.get_status(body)

    def open_box(self, item_name, csrf_token):
        link = COWSEP_WEBSITE + "/crates.php?crate=" + item_name + "&csrf_token=" + csrf_token
        print(link)
        self.driver.get(link)
        body = self.driver.find_element_by_xpath("/html/body").text

        return self.get_status(body)

    def do_twitch_login_for_cowsep(self):
        driver = self.driver
        driver.get(COWSEP_WEBSITE)

        login_link = driver.find_element_by_css_selector("a[href='login.php']")
        login_link.click()
        time.sleep(3)
        login_box = driver.find_element_by_name("login")
        login_box.send_keys(TWITCH_USER)

        pass_box = driver.find_element_by_name("password")
        pass_box.send_keys(TWITCH_PASS)
        pass_box.send_keys(Keys.RETURN)

        time.sleep(2)

    def test_open_boxes(self):
        boxes = { "bullbox", "death_chest", "cowchest2015" }

        for box in boxes:
            process_box = True
            while process_box == True:
                csrf_token = self.get_new_csrf_token()
                process_box = self.open_box(box, csrf_token)


    def get_new_csrf_token(self):
        driver = self.driver
        driver.get(COWSEP_WEBSITE)
        time.sleep(1)
        elem = driver.find_element_by_name("csrf-token")
        csrf_token = elem.get_attribute("content")
        return csrf_token

    def tearDown(self):
        #self.driver.close()
        print("bye!")

if __name__ == "__main__":
    unittest.main()

