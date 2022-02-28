from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def speakers(self):
        self.general_wait()
        return self.driver.find_element(By.ID, 'speakersImg')

    def tablets(self):
        return self.driver.find_element(By.ID, 'tabletsImg')

    def headphones(self):
        return self.driver.find_element(By.ID, 'headphonesImg')

    def laptops(self):
        return self.driver.find_element(By.ID, 'laptopsImg')

    def mice(self):
        return self.driver.find_element(By.ID, 'miceImg')

    def homepage_icon(self):
        return self.driver.find_element(By.XPATH, "//div/a[@href='#/'][@role='link']")

# ================================NAVIGATION STARTS HERE====================================

    def our_products(self):
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='OUR PRODUCTS']")

    def special_offer(self):
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='SPECIAL OFFER']")

    def popular_items(self):
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='POPULAR ITEMS']")

    def contact_us(self):
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='CONTACT US']")

    def search_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[title=SEARCH]>svg[id='menuSearch']")

    def search_bar(self):
        return self.driver.find_element(By.ID, "autoComplete")

    def account_icon(self):
        return self.driver.find_element(By.ID, "menuUserLink")

    def cart_icon(self):
        return self.driver.find_element(By.ID, "menuCart")

    def help_icon(self):
        return self.driver.find_element(By.ID, "menuHelp")

    def about(self):
        self.general_wait()
        self.help_icon().click()
        return self.driver.find_element(By.XPATH, "//div[@id='helpMiniTitle']/label[text()='About']")

    def AOS_Versions(self):
        self.general_wait()
        self.help_icon().click()
        return self.driver.find_element(By.XPATH, "//div[@id='helpMiniTitle']/label[text()='AOS Versions']")

    def Management_Console(self):
        self.general_wait()
        self.help_icon().click()
        return self.driver.find_element(By.XPATH, "//div[@id='helpMiniTitle']/label[text()='Management Console']")



# ======================================WORK FLOWS=======================================
    def search_items(self, search):
        self.search_button().click()
        self.wait_search_bar()
        self.search_bar().send_keys(search)
        self.search_bar().send_keys(Keys.ENTER)

    def create_user(self):
        self.account_icon().click()
        self.driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
# ======================================WAITS=======================================
    def wait_search_bar(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'autoComplete')))

    def general_wait(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='css/images/Special-offer.jpg']")))
