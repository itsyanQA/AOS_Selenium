from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Items:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def product_price(self):
        '''Returns the price element'''
        return self.driver.find_element(By.XPATH, "//div[@class='half']/h2").text

    def colors_info(self):
        '''waits until loading is over, goes over the list of colors available in the product's specific color
        pallet, print to us each color available for the product'''
        self.general_wait()
        list_of_colors = self.list_of_colors()
        for color in list_of_colors:
            print(color.accessible_name)

    def list_of_colors(self):
        '''returns a list of each color in the products color pallet'''
        self.general_wait()
        return self.driver.find_elements(By.XPATH, '//div[@class=""]/span')

    def quantity(self):
        '''returns the quantity element in the product page'''
        self.general_wait()
        return self.driver.find_element(By.NAME, "quantity")

    def change_quantity(self, num):
        '''this function get a number as a param, and changes the quantity according to the number'''
        self.general_wait()
        self.quantity().click()
        self.quantity().send_keys(num)

    def choose_color(self, color):
        '''this function gets a color as a param, and changes the color according to the color we chose, if the color
        doesnt exist, it will choose a color that is available for the product, usually the first one.'''
        self.general_wait()
        list_of_colors = self.list_of_colors()
        for i in list_of_colors:
            if i.accessible_name == color:
                return i.click()

    def add_to_cart(self):
        '''this function returns the add to cart element'''
        self.general_wait()
        return self.driver.find_element(By.XPATH, '//div[@class="fixedBtn"]/button')

    def item_flow(self, num, color):
        '''This function is responsible for item adding flow, waiting until
        loading is over and then choosing quantity, color, and pressing add to cart'''
        self.general_wait()
        self.change_quantity(num)
        self.choose_color(color)
        self.add_to_cart().click()

    def general_wait(self):
        '''waiting until loading stops'''
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))

    def item_total_calculator(self):
        '''Gets the price of the product without dollar signs and commas, and multiplies
        the price by the quantity, the function returns the result.'''
        qty = self.quantity().get_attribute('value')
        price = self.product_price()
        # removes dollar sign and comma from price, converts them to float and multiplies the price times quantity,
        # returns the total
        if '$' or ',' in price:
            new_price = price.replace('$', '').replace(',', '')
            total = float(new_price) * float(qty)
            return total

    def format_returner(self, num1, num2, num3):
        '''Gets 3 different numbers, adding them up and returns the number with dollar sign and commas
        aids us in the test 5 comparison'''
        result = num1 + num2 + num3
        return "${:,.2f}".format(result)
