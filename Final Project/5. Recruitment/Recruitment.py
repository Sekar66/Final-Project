from hashlib import new
from select import select
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class Testrecruitment(unittest.TestCase):  # TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Add Candidates
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

        # Recruitment Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Input
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys("Klara")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input").send_keys("Bohringer")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys("Klara@gmail.com")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click()
        time.sleep(1)

    # Add Candidates empty email
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

        # Recruitment Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Input
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys("Klara")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input").send_keys("Bohringer")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys("")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click()
        time.sleep(1)

    # Search Candidates
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

        # Recruitment Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Input
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("Klara")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]").click()
        time.sleep(1)

    # Reset Search Candidates
    def test_d(self):
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

        # Recruitment Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Input
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("Klara")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]").click()
        time.sleep(1)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
