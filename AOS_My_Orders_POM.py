from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class My_Orders:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def my_orders_product_name(self, row):
        '''Returns the product name in the my orders page'''
        name = self.driver.find_elements(By.XPATH, "//tr/td/span[@class='ng-binding']")
        return name[row].text

    def order_number(self, row):
        '''return the order number of the first order in my orders page'''
        self.general_wait()
        order = self.driver.find_elements(By.XPATH, "//tr/td[1]/label")
        return order[row].text

    def delete_order(self, row):
        '''return the delete order element in my orders page, gets specific row as param'''
        delete = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="remove red ng-scope"]')
        return delete[row]

    def delete_order_confirmation(self):
        '''return the element of the delete order confirmation'''
        return self.driver.find_element(By.ID, 'confBtn_1')

    def general_wait(self):
        '''waiting until loading stops'''
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))

