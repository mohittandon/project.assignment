import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
service = Service()
options= Options()
driver_service = Service(executable_path="/usr/bin/chromedriver")


class TestWebsiteLoad(unittest.TestCase):
 

    # Define a method to test website loading
    def test_load_website(self):
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=driver_service, options=options) # Use any browser driver of your choice.
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        driver.get("https://atg.world/")
        print(driver.title)
        driver.quit()
