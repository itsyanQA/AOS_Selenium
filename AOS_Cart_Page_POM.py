from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Cart_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def shopping_cart_top_left(self):
        '''this function returns the text of the shopping cart nav bar in the cart page'''
        cart = self.driver.find_element(By.CSS_SELECTOR, "a[class='select  ng-binding']")
        return cart.text

    def total_price(self):
        '''this function returns the text of the total price in the cart page'''
        total = self.driver.find_element(By.XPATH, "//td[@colspan='2']/span[2]")
        return total.text

    def edit_button(self, row):
        '''this function returns the edit button in the cart page, according to the row we specified'''
        self.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, 'table[ng-show="cart.productsInCart.length > 0"]')))
        edits = self.driver.find_elements(By.LINK_TEXT, 'EDIT')
        return edits[row]

    def quantity(self,row):
        '''this function returns the quantity in the cart page, according to the row we specified'''
        qty = self.driver.find_elements(By.XPATH, "//tr[@class='ng-scope']/td/label[@class='ng-binding']")
        return qty[row].text

    def checkout_button(self):
        '''this function returns the checkout button in the cart page'''
        return self.driver.find_element(By.ID, 'checkOutButton')

    def existing_acc_username(self):
        '''this function returns the existing acc username, after hitting checkout in the cart page'''
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")

    def existing_acc_password(self):
        '''this function returns the existing acc password, after hitting checkout in the cart page'''
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")

    def login_button(self):
        '''this function returns the login button element, after its clickable'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'login_btnundefined')))
        return self.driver.find_element(By.ID, 'login_btnundefined')

    def sign_in_existing_acc_flow(self, username, password):
        '''this flow handles the sign in using existing account after hitting checkout in the cart page,
        it gets username and password as params, and then hits the login button.'''
        self.existing_acc_username().send_keys(username)
        self.existing_acc_password().send_keys(password)
        self.login_button().click()

    def product_name(self, row):
        '''Gets a row as param, returns the product name according to the row specified'''
        name = self.driver.find_elements(By.CSS_SELECTOR, '[class="roboto-regular productName ng-binding"]')
        return name[row].text

    def product_quantity(self, row):
        '''Gets a row as param, returns the product quantity according to the row specified'''
        quantity = self.driver.find_elements(By.XPATH, "//td[@class='smollCell quantityMobile']/label[2]")
        return quantity[row].text

    def product_price(self, row):
        '''Gets a row as param, returns the product price according to the row specified'''
        price = self.driver.find_elements(By.XPATH, "//td[@class='smollCell']/p")
        return price[row].text

