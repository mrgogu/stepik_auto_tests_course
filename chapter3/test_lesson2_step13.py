from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

TEST_CASE = {
    "first name": "Ivan",
    "last name": "Ivanov",
    "email": "mail@example.org"
    }

class MyTest(unittest.TestCase):
    def test_reg_1(self):
        link = "http://suninjuly.github.io/registration1.html"        
        browser = webdriver.Chrome()
        browser.get(link)
        requred_elements = browser.find_elements(By.CSS_SELECTOR,'[required]')
        input_first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input_first_name.send_keys(TEST_CASE.get("first name"))    

        input_last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input_last_name.send_keys(TEST_CASE.get("last name"))    
        
        input_email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input_email.send_keys(TEST_CASE.get("email"))        

        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text    
        self.assertEqual( "Congratulations! You have successfully registered!", welcome_text, f"Fail test 1: on link {link}")
        time.sleep(10)
        browser.quit()
    
    def test_reg_2(self):
        TEST_CASE = ["Ivan", "Ivanov", "mail@example.org"]
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input_first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input_first_name.send_keys(TEST_CASE.get("first name"))    

        input_last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input_last_name.send_keys(TEST_CASE.get("last name"))    
        
        input_email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input_email.send_keys(TEST_CASE.get("email"))        

        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text    
        self.assertEqual( "Congratulations! You have successfully registered!", welcome_text, f"Fail test 2: on link {link}")
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
