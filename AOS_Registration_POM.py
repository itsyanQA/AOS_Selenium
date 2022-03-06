from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *


class Registration:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def registration_button(self):
        '''Returns the registration button element when checking out a product when not logged-in'''
        return self.driver.find_element(By.ID, 'registration_btnundefined')

    def username(self):
        '''Returns the username element'''
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="usernameRegisterPage"][type="text"]')

    def password(self):
        '''Returns the password element'''
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="passwordRegisterPage"][type="password"]')

    def confirm_password(self):
        '''Returns the confirm password element'''
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="confirm_passwordRegisterPage"][type="password"]')

    def email(self):
        '''Returns the email element'''
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="emailRegisterPage"][type="text"]')

    def terms(self):
        '''Return the terms checkbox element'''
        self.wait_for_terms_to_be_clickable()
        return self.driver.find_element(By.NAME, "i_agree")

    def register(self):
        '''Waits until register button is clickable, and then returns the register button'''
        # tries to find the register button element, if a Timeoutexception occurs, we catch that in the except block
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, 'register_btnundefined')))
            return self.driver.find_element(By.ID, 'register_btnundefined')
        # after catching the exception, we click on terms again, and return the register button element.
        except TimeoutException:
            self.terms().click()
            self.wait.until(EC.element_to_be_clickable((By.ID, 'register_btnundefined')))
            return self.driver.find_element(By.ID, 'register_btnundefined')


    def account_details(self, user, password, conf_pass, email):
        '''this flow handles user creation, it gets user,password,confirm password and email as params, and it
        click on terms multiple times until it is checked because of site delay using a while loop.'''
        self.general_wait()
        self.username().send_keys(user)
        self.password().send_keys(password)
        self.confirm_password().send_keys(conf_pass)
        self.email().send_keys(email)


    def general_wait(self):
        '''waiting until loading stops'''
        self.wait.until(EC.invisibility_of_element((By.XPATH,"//div[@class='loader']")))

    def wait_for_terms_to_be_clickable(self):
        '''waits until the terms checkbox is clickable'''
        self.wait.until(EC.element_to_be_clickable((By.NAME, 'i_agree')))

