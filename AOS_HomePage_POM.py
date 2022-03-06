from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

class HomePage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def speakers(self):
        '''This function returns the speakers element'''
        self.general_wait()
        return self.driver.find_element(By.ID, 'speakersImg')

    def tablets(self):
        '''This function returns the tablets element'''
        self.general_wait()
        return self.driver.find_element(By.ID, 'tabletsImg')

    def headphones(self):
        '''This function returns the headphones element'''
        self.general_wait()
        return self.driver.find_element(By.ID, 'headphonesImg')

    def laptops(self):
        '''This function returns the laptops element'''
        self.general_wait()
        return self.driver.find_element(By.ID, 'laptopsImg')

    def mice(self):
        '''This function returns the mice element'''
        self.general_wait()
        return self.driver.find_element(By.ID, 'miceImg')

    def category_clicker(self, category):
        '''This function returns the specific category we mentioned in the parameter, we use this function in the
        excel unittests'''
        self.general_wait()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'categoryCell')))
        categories = self.driver.find_elements(By.CLASS_NAME, 'categoryCell')
        for i in categories:
            if i.text == category:
                return i

    def homepage_icon(self):
        '''Return the AOS logo homepage element'''
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//div/a[@href='#/'][@role='link']")

# ================================NAVIGATION STARTS HERE====================================

    def our_products(self):
        '''This function return the our products element'''
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='OUR PRODUCTS']")

    def special_offer(self):
        '''This function return the special offer element'''
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='SPECIAL OFFER']")

    def popular_items(self):
        '''This function return the popular items element'''
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='POPULAR ITEMS']")

    def contact_us(self):
        '''This function return the contact us element'''
        self.general_wait()
        return self.driver.find_element(By.XPATH, "//li/a[text()='CONTACT US']")

    def search_button(self):
        '''This function return the search icon element'''
        self.general_wait()
        return self.driver.find_element(By.CSS_SELECTOR, "a[title=SEARCH]>svg[id='menuSearch']")

    def search_bar(self):
        '''This function return the search bar element'''
        self.general_wait()
        return self.driver.find_element(By.ID, "autoComplete")

    def account_icon(self):
        '''This function returns the account icon element'''
        self.general_wait()
        return self.driver.find_element(By.ID, "menuUserLink")

    def my_account(self):
        '''This function returns my account element inside the account drop down menu'''
        self.general_wait()
        self.account_icon().click()
        return self.driver.find_element(By.CSS_SELECTOR, 'label[translate="My_account"][role=link]')

    def delete_account(self):
        '''This function returns the delete account option inside my account page'''
        self.general_wait()
        return self.driver.find_element(By.CLASS_NAME, 'deleteBtnText')

    def delete_account_confirmation(self):
        self.general_wait()
        return self.driver.find_element(By.CSS_SELECTOR, '[class="deletePopupBtn deleteRed"]')

    # ======================================POP-UP WINDOW - SIGN IN =======================================
    def existing_username(self):
        '''This fucntion returns the username inside the sign-in pop up window'''
        return self.driver.find_element(By.NAME, 'username')

    def existing_password(self):
        '''This fucntion returns the password inside the sign-in pop up window'''
        return self.driver.find_element(By.NAME, 'password')

    def sign_in_button(self):
        '''This fucntion returns the sign in button element inside the sign-in pop up window'''
        return self.driver.find_element(By.ID, 'sign_in_btnundefined')

    def exit_button(self):
        '''This function returns the "X" button in the sign in pop up window'''
        return self.driver.find_element(By.CLASS_NAME, 'closeBtn')
    # ====================================================================================================

    def sign_out_button(self):
        '''This function returns the "Sign-Out" from the account drop down menu.'''
        return self.driver.find_element(By.XPATH, "//label[text()='Sign out' and @href='javascript:void(0)']")

    def username_proof(self):
        '''This function servers us for the tenth task, it returns the current user name'''
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="hi-user containMiniTitle ng-binding"]')))
        user = self.driver.find_element(By.CSS_SELECTOR, '[class="hi-user containMiniTitle ng-binding"]')
        return user.text

    def my_orders(self):
        '''This function returns the "My Orders" from the account drop down menu.'''
        return self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][class='option ng-scope'][role='link']")

    def cart_icon(self):
        '''This function returns the cart icon element'''
        self.general_wait()
        return self.driver.find_element(By.ID, "menuCart")

    def help_icon(self):
        '''This function returns the help icon element'''
        self.general_wait()
        return self.driver.find_element(By.ID, "menuHelp")

    def about(self):
        '''This function opens the About page'''
        self.general_wait()
        self.help_icon().click()
        return self.driver.find_element(By.XPATH, "//div[@id='helpMiniTitle']/label[text()='About']")

    def AOS_Versions(self):
        '''This function opens AOS Versions page'''
        self.general_wait()
        self.help_icon().click()
        return self.driver.find_element(By.XPATH, "//div[@id='helpMiniTitle']/label[text()='AOS Versions']")

    def Management_Console(self):
        '''This function opens management console'''
        self.general_wait()
        self.help_icon().click()
        return self.driver.find_element(By.XPATH, "//div[@id='helpMiniTitle']/label[text()='Management Console']")



# ======================================WORK FLOWS=======================================
    def search_items(self, search):
        '''This function searches items in the search bar, it gets an input for search as a param.'''
        self.search_button().click()
        self.wait_search_bar()
        self.search_bar().send_keys(search)
        self.search_bar().send_keys(Keys.ENTER)

    def create_user(self):
        '''This function leads us to the create a new user page'''
        self.account_icon().click()
        self.driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()

    def login_existing_user(self,username, password):
        '''This function handles the login using existing user flow, it gets username and password as params'''
        self.account_icon().click()
        self.existing_username().send_keys(username)
        self.existing_password().send_keys(password)
        self.sign_in_button().click()

    def log_out_flow(self):
        '''This function handles the log out flow'''
        self.general_wait()
        # we put the function in a while loop because sometimes the site is too quick and the clicks dont register,
        # the while loop is to make sure we click on account icon and sign out.
        while True:
            try:
                self.account_icon().click()
                self.sign_out_button().click()
                break
            except ElementClickInterceptedException:
                pass

    def delete_account_flow(self):
        '''This function handles the delete account flow, enters the account profile and deletes the account'''
        self.account_icon().click()
        self.my_account().click()
        self.delete_account().click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="deletePopupBtn deleteRed"]')))
        # waiting until the confirm pop up window shows
        self.delete_account_confirmation().click()

# ======================================WAITS=======================================
    def wait_search_bar(self):
        '''Waits until the search bar appears'''
        return self.wait.until(EC.visibility_of_element_located((By.ID, 'autoComplete')))

    def general_wait(self):
        '''Waits until Loader (loading screen) disappears'''
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))

    def sign_in_window_wait(self):
        '''Waits until we can see "Forgot Your Password" element'''
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="forgot-Passwowd ng-scope"]')))

    def homepage_full_load(self):
        '''Waits until the element of the user name disappears.'''
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//a[@class='img']/span[@data-ng-show='userCookie.response']")))

    def wait_until_pop_up_goes_away(self):
        '''Wait until the delete account pop-up window disappears'''
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "PopUp")))

