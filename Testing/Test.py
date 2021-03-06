# import all required frameworks
from time import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# inherit TestCase Class and create a new test class


class RunningTest(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(
            r"D:\BE\BE Project\BEProjectProgress\LoanApprovalStatus\Test\Testing\chromedriver.exe")

    # Test case method. It should always start with test_
    def test_url_test(self):

        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        # assertion to confirm if title has python keyword in it
        self.assertIn("Bank", driver.title)

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()


class UserLogin(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(
            r"D:\BE\BE Project\BEProjectProgress\LoanApprovalStatus\Test\Testing\chromedriver.exe")

    def test_user_login(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.NAME,
            "user[email]").send_keys("new@gmail.com")
        driver.find_element(By.NAME, "user[password]").send_keys("1234")
        driver.find_element(By.XPATH,
            "/html/body/div[2]/div[2]/div[1]/form/input[3]").click()
        driver.implicitly_wait(100)
        driver.implicitly_wait(2)
        self.assertEquals("User Dashboard", driver.title)

    def test_user_login_validOne(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.NAME,
                            "user[email]").send_keys("new@gmail.com")
        driver.find_element(By.NAME, "user[password]").send_keys("12345")
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[2]/div[1]/form/input[3]").click()
        driver.implicitly_wait(100)
        driver.implicitly_wait(2)
        self.assertNotEquals("User Dashboard", driver.title)

    def test_user_login_validTwo(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.NAME,
                            "user[email]").send_keys("new1@gmail.com")
        driver.find_element(By.NAME, "user[password]").send_keys("1234")
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[2]/div[1]/form/input[3]").click()
        driver.implicitly_wait(100)
        driver.implicitly_wait(2)
        self.assertEquals("User Dashboard", driver.title)

    def test_user_login_validThree(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.NAME,
                            "user[email]").send_keys("new1@gmail.com")
        driver.find_element(By.NAME, "user[password]").send_keys("1234")
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[2]/div[1]/form/input[3]").click()
        driver.implicitly_wait(100)
        driver.implicitly_wait(2)
        self.assertEquals("User Dashboard", driver.title)

    def test_user_check_status(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.NAME,
                            "user[email]").send_keys("new@gmail.com")
        driver.find_element(By.NAME, "user[password]").send_keys("1234")
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[2]/div[1]/form/input[3]").click()
        driver.implicitly_wait(2)
        driver.find_element(
            By.XPATH, "/html/body/div[2]/header/nav/ul[1]/li[1]/a").click()
        driver.implicitly_wait(25)
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/ul/li[3]/a/span").click()
        driver.implicitly_wait(25)

    def test_user_loan_status(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.NAME,
                            "user[email]").send_keys("new@gmail.com")
        driver.find_element(By.NAME, "user[password]").send_keys("1234")
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[2]/div[1]/form/input[3]").click()
        driver.implicitly_wait(2)
        driver.find_element(
            By.XPATH, "/html/body/div[2]/header/nav/ul[1]/li[1]/a").click()
        driver.implicitly_wait(25)
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/ul/li[4]/a/span").click()
        driver.implicitly_wait(25)

    def tearDown(self):
        self.driver.close()
    # cleanup method called after every test performed

    def test_user_logout(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.NAME,
            "user[email]").send_keys("new@gmail.com")
        driver.find_element(By.NAME, "user[password]").send_keys("1234")
        driver.find_element(By.XPATH,
            "/html/body/div[2]/div[2]/div[1]/form/input[3]").click()
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/header/nav/ul[1]/li[1]/a/i").click()
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[1]/div[3]/div/ul/li[5]/a").click()
        self.assertEquals("Bank", driver.title)

    def tearDown(self):
        self.driver.close()


class AdminLogin(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(
            r"D:\BE\BE Project\BEProjectProgress\LoanApprovalStatus\Test\Testing\chromedriver.exe")

    def test_admin_login(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.XPATH,
            "/html/body/div[1]/div/form/input").click()
        driver.find_element(By.NAME,
            "admin[username]").send_keys("admin101d@gmail.com")
        driver.find_element(By.NAME, "admin[password]").send_keys("admin@101")
        driver.find_element(By.XPATH,
            "/html/body/div[1]/form/div/input").click()
        self.assertEquals("Admin Dashboard", driver.title)

    def test_admin_login_valid(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/form/input").click()
        driver.find_element(By.NAME,
                            "admin[username]").send_keys("admin101d@gmail.com")
        driver.find_element(By.NAME, "admin[password]").send_keys("admin@101")
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/form/div/input").click()
        self.assertEquals("Admin Dashboard", driver.title)

    def tearDown(self):
        self.driver.close()
    # cleanup method called after every test performed

    def test_admin_logout(self):
        # get driver
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        driver.find_element(By.XPATH,
            "/html/body/div[1]/div/form/input").click()
        driver.find_element(By.NAME,
            "admin[username]").send_keys("admin101d@gmail.com")
        driver.find_element(By.NAME, "admin[password]").send_keys("admin@101")
        driver.find_element(By.XPATH,
            "/html/body/div[1]/form/div/input").click()
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/header/nav/ul[1]/li[1]/a/i").click()
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div[1]/div[3]/div/ul/li[4]/a").click()
        self.assertEquals("Bank", driver.title)
    # cleanup method called after every test performed

    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()
