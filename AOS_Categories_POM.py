from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Categories:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

# =============================Actions================================
    def speakers_items(self, index):
        '''this function gets index as a param, and enters the product accordingly in speaker category'''
        self.general_wait()
        speaker_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        speaker_items[index].click()

    def tablets_items(self, index):
        '''this function gets index as a param, and enters the product accordingly in tablet category'''
        self.general_wait()
        tablet_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        tablet_items[index].click()

    def headphones_items(self, index):
        '''this function gets index as a param, and enters the product accordingly in headphones category'''
        self.general_wait()
        headphones_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        headphones_items[index].click()

    def laptops_items(self, index):
        '''this function gets index as a param, and enters the product accordingly in laptops category'''
        self.general_wait()
        laptops_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        laptops_items[index].click()

    def mice_items(self, index):
        '''this function gets index as a param, and enters the product accordingly in mice category'''
        self.general_wait()
        mice_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        mice_items[index].click()

# =============================INFORMATION ABOUT THE ITEMS================================

    def speakers_info(self):
        '''returns the index of the item and its name'''
        self.general_wait()
        speaker_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        for item in speaker_items:
            print(f"{speaker_items.index(item)}: {item.text}")

    def tablets_info(self):
        '''returns the index of the item and its name'''
        self.general_wait()
        tablet_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        for item in tablet_items:
            print(f"{tablet_items.index(item)}: {item.text}")

    def headphones_info(self):
        '''returns the index of the item and its name'''
        self.general_wait()
        headphones_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        for item in headphones_items:
            print(f"{headphones_items.index(item)}: {item.text}")

    def laptops_info(self):
        '''returns the index of the item and its name'''
        self.general_wait()
        laptops_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        for item in laptops_items:
            print(f"{laptops_items.index(item)}: {item.text}")

    def mice_info(self):
        '''returns the index of the item and its name'''
        self.general_wait()
        mice_items = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="productName ng-binding"]')
        for item in mice_items:
            print(f"{mice_items.index(item)}: {item.text}")

    def general_wait(self):
        '''waiting until loading stops'''
        self.wait.until(EC.invisibility_of_element((By.XPATH,"//div[@class='loader']")))








