from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from AOS_HomePage_POM import HomePage


class Checkout:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)
        self.homepage = HomePage(self.driver)

    def next_button(self):
        '''returns the element of "NEXT" button after logging in'''
        self.general_wait()
        return self.driver.find_element(By.ID, 'next_btn')

    def edit_payment(self):
        '''return the element of "edit" button when making a purchase'''
        return self.driver.find_element(By.CSS_SELECTOR, 'label[data-ng-click="toggleShowMasterCart()"]')

    # ================================SAFEPAY METHODS====================================
    def safepay_radio_box(self):
        '''returns the element of safepay radio box'''
        return self.driver.find_element(By.NAME, 'safepay')

    def safepay_username(self):
        '''returns the element of safepay username'''
        return self.driver.find_element(By.NAME, 'safepay_username')

    def safepay_password(self):
        '''returns the element of safepay password'''
        return self.driver.find_element(By.NAME, 'safepay_password')

    def pay_now_button_safepay(self):
        '''return the element of safepay pay now button'''
        return self.driver.find_element(By.ID, 'pay_now_btn_SAFEPAY')

    def safepay_flow(self, username, password):
        '''flow handles making a purchase using safepay method, get password and username as params'''
        self.general_wait()
        self.safepay_radio_box().click()
        self.safepay_username().send_keys(username)
        self.safepay_password().send_keys(password)
        self.pay_now_button_safepay().click()

    # ================================SAFEPAY METHODS====================================

    # ================================CREDIT CARD METHODS STARTS HERE====================================
    def master_credit_checkbox(self):
        '''returns master_credit checkbox element'''
        return self.driver.find_element(By.NAME, 'masterCredit')

    def card_number(self):
        '''return card number element'''
        return self.driver.find_element(By.ID, 'creditCard')

    def cvv(self):
        '''returns cvv element'''
        self.general_wait()
        return self.driver.find_element(By.NAME, 'cvv_number')

    def MM(self):
        '''returns MM element with a drop down list'''
        mm_dropdown = self.driver.find_element(By.NAME, 'mmListbox')
        mm = Select(mm_dropdown)
        return mm

    def YYYY(self):
        '''returns YYYY element with a drop down list'''
        yy_dropdown = self.driver.find_element(By.NAME, 'yyyyListbox')
        yyyy = Select(yy_dropdown)
        return yyyy

    def cardholder_name(self):
        '''returns card holder name element'''
        return self.driver.find_element(By.NAME, 'cardholder_name')

    def pay_now_button_credit_card(self):
        '''returns the pay now button element when using a credit card'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'pay_now_btn_ManualPayment')))
        return self.driver.find_element(By.ID, 'pay_now_btn_ManualPayment')

    def save_for_future_use(self):
        '''returns the "save for future use" checkbox element when using a credit card'''
        return self.driver.find_element(By.NAME, 'save_master_credit')

    def master_credit_flow_future_use_checked(self, card_number, cvv, mm, yyyy, cardholder_name):
        '''this function handles the pay with master credit flow, it
         gets cardnumber, cvv, mm, yyyy, cardholder name as params and makes a purchase,
         plus checking "save for future use"'''
        self.master_credit_checkbox().click()
        self.card_number().send_keys(card_number)
        # By default, the first number doesnt register properly, we clear the cvv field first, then enter
        # the 3 digits
        self.cvv().clear()
        self.cvv().send_keys(cvv)
        self.MM().select_by_visible_text(mm)
        self.YYYY().select_by_visible_text(yyyy)
        self.cardholder_name().clear()
        # We need to clear the name since it is saved from last time
        self.cardholder_name().send_keys(cardholder_name)
        self.pay_now_button_credit_card().click()

    def master_credit_flow_uncheck_for_future_use(self, card_number, cvv, mm, yyyy, cardholder_name):
        '''this function handles the pay with master credit flow, it
        gets cardnumber, cvv, mm, yyyy, cardholder name as params and makes a purchase,
        without checking "save for future use"'''
        self.master_credit_checkbox().click()
        self.card_number().send_keys(card_number)
        self.cvv().send_keys(cvv)
        # if the cvv doesnt match the cvv we intended to, it clears the field and sends the keys again.
        if self.cvv().get_attribute('value') != cvv:
            self.cvv().clear()
            self.cvv().send_keys(cvv)
        self.MM().select_by_visible_text(mm)
        self.YYYY().select_by_visible_text(yyyy)
        self.cardholder_name().send_keys(cardholder_name)
        self.save_for_future_use().click()
        self.pay_now_button_credit_card().click()

    # ================================CREDIT CARD METHODS ENDS HERE====================================

    def order_number_from_completion_page(self):
        '''finds the order number for payment successful page'''
        self.general_wait()
        return self.driver.find_element(By.ID, 'orderNumberLabel').text

    def general_wait(self):
        '''waiting until loading stops'''
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))

    def wait_for_payment_success_window(self):
        '''wait until the payment successful page fully loads'''
        self.wait.until(EC.visibility_of_element_located((By.ID, 'orderPaymentSuccess')))
