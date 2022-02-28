from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Cart:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def cart_items_from_nav(self):
        '''print the current amount of items in the cart from the navigation bar'''
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')))
        total_items = self.driver.find_element(By.XPATH, '//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')
        print(total_items.text)
