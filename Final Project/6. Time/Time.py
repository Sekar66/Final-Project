from hashlib import new
from select import select
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class Testtime(unittest.TestCase):  # TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Search Timesheets with valid format
    def test_a(self):
        # steps
        browser = self.browser  # buka web browser
        # buka situs
        browser.get(
            "https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        # Login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # Time Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(1)

        # Search Timesheets
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("Linda Jane Anderson")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('Found', response_message)

    # Search Timesheets with random name format
    def test_b(self):
        # steps
        browser = self.browser  # buka web browser
        # buka situs
        browser.get(
            "https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        # Login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # Time Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(1)

        # Search Timesheets
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("Zaza zizi")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/span").text

        self.assertIn('Required', response_message)

    # Search Timesheets with Empty name
    def test_c(self):
        # steps
        browser = self.browser  # buka web browser
        # buka situs
        browser.get(
            "https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        # Login
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # Time Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(1)

        # Search Timesheets
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/span").text

        self.assertIn('Required', response_message)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
