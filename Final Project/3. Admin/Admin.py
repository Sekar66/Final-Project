from hashlib import new
from select import select
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class TestAdmin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Add Employee with valid format
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Add button
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa  Andrews")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Andrew.Lisa")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)

    # Add Employee with Empty User Role
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Add button
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").send_keys("")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa  Andrews")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Andrew.Lisa")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)

    # Add Employee with empty Employee name
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Add button
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Andrew.Lisa")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)

    # Add Employee with Empty Status
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Add button
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa  Andrews")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Andrew.Lisa")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)

    # Add Employee with emptyusername
    def test_e(self):
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Add button
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa  Andrews")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)

    # Add Employee with empty password
    def test_f(self):
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Add button
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa  Andrews")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Andrew.Lisa")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)

    # Add Employee with empty confirm password
    def test_g(self):
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Add button
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").send_keys("Admin")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa  Andrews")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Andrew.Lisa")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa123*")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)

    # Search User data
    def test_j(self):
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Fiona.Grace")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "//html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(1)

    # Reset User data
    def test_k(self):
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

        # Admin Menu
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        # Adding Data
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Fiona.Grace")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click()
        time.sleep(1)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
