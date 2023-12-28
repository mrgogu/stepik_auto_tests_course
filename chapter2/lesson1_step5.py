import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LINK =  "https://suninjuly.github.io/math.html"

class MyPage(webdriver.Chrome):
    def __init__(self,link):
        super().__init__()
        self.get(link)
        self.x = self.find_x()

    def find_x(self):
        return self.find_element(By.CSS_SELECTOR, "#input_value").text
    
    def calc(self):
        return str(math.log(abs(12*math.sin(int(self.x)))))
    
    def input_answer(self):
        answer = self.calc()
        answer_input = self.find_element(By.CSS_SELECTOR, "#answer")
        answer_input.send_keys(answer)
        
    def click_checkbox(self):
        return self.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    
    def click_radiobutton(self):
        return self.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    
    def click_submit(self):
        return self.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        

    
if __name__ == "__main__":
    test = MyPage(LINK)
    try:        
        test.input_answer()
        test.click_checkbox()
        test.click_radiobutton()
        test.click_submit()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        test.quit()