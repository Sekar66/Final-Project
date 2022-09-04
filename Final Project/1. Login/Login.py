import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Input valid Username and Password
    def test_a_success_login(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

    # Input Invalid Username and Password
    def test_b_fail_login_by_invalid_email_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Sanber")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("Code123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text

        # Cannot login
        self.assertIn('Invalid', response_message)

    # Input Invalid Username
    def test_c_fail_login_by_invalid_email(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Sanber")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text

        # Cannot login
        self.assertIn('Invalid', response_message)

    # Input Invalid Password
    def test_d_fail_login_by_invalid_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("Code123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text

        # Cannot login
        self.assertIn('Invalid', response_message)

    # Input Empty Username and Password
    def test_e_fail_login_with_empty_email_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text

        # Cannot login
        self.assertIn('Required', response_message)

    # Input Empty Username
    def test_f_fail_login_with_empty_email(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text

        # Cannot login
        self.assertIn('Required', response_message)

    # Input Empty Password
    def test_b_fail_login_with_empty_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")  # isi Username
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("")  # isi password
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)

        # validation
        response_message = browser.find_element(
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text

        # Cannot login
        self.assertIn('Required', response_message)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
