from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from AOS_Selenium.AOS_HomePage_POM import HomePage
from AOS_Selenium_Automation.AOS_Categories_POM import Categories
from AOS_Selenium_Automation.AOS_Items_POM import Items
from AOS_Cart_POM import Cart


service_chrome = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)

homepage = HomePage(driver)
categories = Categories(driver)
item = Items(driver)
cart = Cart(driver)


driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)



# homepage.speakers().click()
# categories.speakers_info()
# categories.speakers_items(0)
#
# item.colors_info()
# item.choose_color('GRAY')
# item.change_quantity('6')
# item.add_to_cart().click()
# sleep(2)
# cart.cart_items_from_nav()
# homepage.search_items('hello')


