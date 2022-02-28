from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from random import *

class Items:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def colors_info(self):
        list_of_colors = self.list_of_colors()
        for color in list_of_colors:
            print(color.accessible_name)

    def list_of_colors(self):
        return self.driver.find_elements(By.XPATH, '//div[@class=""]/span')

    def quantity(self):
        return self.driver.find_element(By.NAME, "quantity")

    def change_quantity(self, num):
        self.quantity().click()
        self.quantity().send_keys(num)

    def choose_color(self, color):
        list_of_colors = self.list_of_colors()
        for i in list_of_colors:
            if i.accessible_name == color:
                i.click()

    def add_to_cart(self):
        return self.driver.find_element(By.XPATH, '//div[@class="fixedBtn"]/button')









