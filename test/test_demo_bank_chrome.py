import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options   # Import a different options class to run on a different browser
from test import base_test


class TestDemoBank(base_test.BaseTest):

    testName = 'Demo Bank Chrome Test'
    options = Options()
    driver = None

    def setUp(self):
        super().setUp()

        self.options.set_capability('digitalai:testName', self.testName)
        self.driver = webdriver.Remote(self.getUrl(), options=self.options)

    def testQuickStartIosNativeDemo(self):
        self.driver.get('https://demo-bank.ct.digital.ai')

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'login')))

        self.driver.find_element(By.XPATH, "//*[@data-auto='username']//input").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@data-auto='password']//input").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@data-auto='login']").click()

        self.driver.find_element(By.XPATH, "//*[@data-auto='transfer-funds']").click()

        self.driver.find_element(By.XPATH, "//input[@name='NAME']").send_keys('John')
        self.driver.find_element(By.XPATH, "//input[@name='PHONE']").send_keys('1-234-5678')
        self.driver.find_element(By.XPATH, "//input[@name='AMOUNT']").send_keys('1000')
        self.driver.find_element(By.XPATH, "//*[@data-auto='country']").click()
        self.driver.find_element(By.XPATH, "//*[text()='India']").click()
        self.driver.find_element(By.XPATH, "//*[@data-auto='transfer-button']").click()

    def tearDown(self):
        print('Report URL: ' + self.driver.capabilities['reportUrl'])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
