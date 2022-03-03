from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *


class Cart_Window:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)
        self.action = ActionChains(self.driver)

    def cart_total_items_from_nav(self):
        '''print the current amount of items in the cart from the navigation bar, waits until the small number appears,
        if not then we return 0 because the table is empty.'''
        self.general_wait()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')))
            total_items = self.driver.find_element(By.XPATH,
                                                   '//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')
            return total_items.text
        except TimeoutException:
            return '0'

    def cart_product_name(self, row):
        '''returns a product name according to the row we specified'''
        self.general_wait()
        self.hover()
        name = self.driver.find_elements(By.CSS_SELECTOR,"h3[class='ng-binding']")
        return name[row].text

    def cart_product_quantity(self, row):
        '''returns a product quantity according to the row we specified'''
        self.general_wait()
        self.hover()
        quantity = self.driver.find_elements(By.XPATH, '//a/label[1]')
        return quantity[row].text

    def cart_product_color(self, row):
        '''returns a product color according to the row we specified'''
        self.general_wait()
        self.hover()
        color = self.driver.find_elements(By.XPATH, '//a/label/span')
        return color[row].text

    def cart_product_price(self, row):
        '''returns a product price according to the row we specified'''
        self.general_wait()
        self.hover()
        price = self.driver.find_elements(By.XPATH, "//p[@class='price roboto-regular ng-binding']")
        return price[row].text

    def price_calculator(self, row):
        '''function receives certain row, and multiplies the price X quantity, after calculating we return the
        result putting a dollar sign at the start and commas where needed.'''
        self.hover()
        money = self.driver.find_element(By.XPATH,
                                         "//div[@id='Description']/h2[@class='roboto-thin screen768 ng-binding']")
        price = money.text[1:]
        if ',' in price:
            price = price.replace(',', '')
        qty = self.cart_product_quantity(row)
        qty = qty[4:]
        total = float(price) * int(qty)
        return "${:,.2f}".format(total)

    def hover(self):
        '''This function hovers on the cart icon, so we can have access to the drop down menu'''
        self.general_wait()
        hover = self.driver.find_element(By.ID, 'shoppingCartLink')
        self.action.move_to_element(hover).perform()

    def table_items(self):
        '''return the text of each product in the cart'''
        self.general_wait()
        self.hover()
        try:
            tr = self.driver.find_elements(By.CSS_SELECTOR, "tr[id='product']")
            for i in tr:
                return i.text[:-3]
        except ElementNotInteractableException:
            return 'Table not found'

    def row_finder(self, row):
        '''return the text of each product in the cart, according to the row we specified'''
        self.general_wait()
        self.hover()
        try:
            tr = self.driver.find_elements(By.CSS_SELECTOR, "tr[id='product']")
            return tr[row].text
        except ElementNotInteractableException:
            return 'Table not found'

    def general_wait(self):
        '''waiting until loading stops'''
        self.wait.until(EC.invisibility_of_element((By.XPATH,"//div[@class='loader']")))

    def remove_item(self, row):
        '''This function removes a product from the cart according to the row we specified'''
        self.general_wait()
        self.hover()
        x = self.driver.find_elements(By.CSS_SELECTOR, '.removeProduct')
        return x[row]

    def cart_button(self):
        '''returns the cart icon element'''
        return self.driver.find_element(By.ID, 'menuCart')

    def checkout_button(self):
        '''returns the checkout button element in the cart pop up menu'''
        self.general_wait()
        self.hover()
        return self.driver.find_element(By.ID, 'checkOutPopUp')

    def small_cart_num_disappearance_wait(self):
        '''this function waits until the small number above the cart disappears,
        usually when doing a purchase'''
        self.wait.until(EC.invisibility_of_element((By.XPATH, '//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')))









