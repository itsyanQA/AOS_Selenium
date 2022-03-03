from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from AOS_Cart__Window_POM import Cart_Window
from AOS_Items_POM import Items
from AOS_Categories_POM import Categories
from AOS_HomePage_POM import HomePage
from AOS_Cart_Page_POM import Cart_Page
from AOS_Checkout_POM import Checkout
from AOS_Registration_POM import Registration
from AOS_My_Orders_POM import My_Orders


class AOS_UnitTests(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.cart = Cart_Window(self.driver)
        self.cart_page = Cart_Page(self.driver)
        self.items = Items(self.driver)
        self.categories = Categories(self.driver)
        self.homepage = HomePage(self.driver)
        self.checkout = Checkout(self.driver)
        self.registration = Registration(self.driver)
        self.orders = My_Orders(self.driver)

    def test_1_first_task(self):
        '''This test adds 5 items to the cart, and it verifies that the total item count is 5.'''
        self.homepage.mice().click()
        self.categories.mice_items(0)
        self.items.item_flow(2, 'BLACK')
        '''choosing first item from mices, adding a product with a quantity of 2'''
        self.homepage.homepage_icon().click()
        self.homepage.speakers().click()
        self.categories.speakers_items(0)
        self.items.item_flow(3, 'GRAY')
        '''choosing first item from speakers, adding a product with a quantity of 3'''
        self.assertEqual(self.cart.cart_total_items_from_nav(), '5')
        '''asserts that the total number of items in the cart is 5, 3+2'''

    def test_2_second_task(self):
        '''This test verifies that each product we add to the cart
         matches the correct name, color, price and quantity.'''
        self.homepage.mice().click()
        self.categories.mice_items(0)
        self.items.item_flow(2, 'BLACK')
        # ==============================FIRST PRODUCT====================================
        self.assertEqual(self.cart.cart_product_color(0), 'BLACK')
        self.assertEqual(self.cart.cart_product_name(0), 'HP USB 3 BUTTON OPTICAL MOUSE')
        self.assertEqual(self.cart.cart_product_quantity(0), 'QTY: 2')
        self.assertEqual(self.cart.cart_product_price(0), self.cart.price_calculator(0))
        self.homepage.homepage_icon().click()
        self.homepage.speakers().click()
        self.categories.speakers_items(0)
        self.items.item_flow(3, 'GRAY')
        # ==============================SECOND PRODUCT====================================
        self.assertEqual(self.cart.cart_product_color(0), 'GRAY')
        '''The elements are being stacked instead of being in a certain order, index 0 will
         always be the latest added product, test below proves it'''
        self.assertEqual(self.cart.cart_product_color(1), 'BLACK')
        self.assertIn('BOSE SOUNDLINK BLUETOOTH', self.cart.cart_product_name(0))
        self.assertEqual(self.cart.cart_product_quantity(0), 'QTY: 3')
        self.assertEqual(self.cart.cart_product_price(0), self.cart.price_calculator(0))
        self.homepage.homepage_icon().click()
        self.homepage.tablets().click()
        self.categories.tablets_items(0)
        self.items.item_flow(4, 'BLACK')
        # ==============================THIRD PRODUCT====================================
        self.assertEqual(self.cart.cart_product_color(0), 'BLACK')
        self.assertIn('HP ELITEPAD 1000 G2 TABLET', self.cart.cart_product_name(0))
        self.assertEqual(self.cart.cart_product_quantity(0), 'QTY: 4')
        self.assertIn(self.cart.price_calculator(0), self.cart.cart_product_price(0))
        '''Bug found, when choosing HP elitepad color black, it shows as color BLUE in the cart.'''

    def test_3_third_task(self):
        '''Testing the functionality of the "X" button in cart hover menu'''
        self.homepage.tablets().click()
        self.categories.tablets_items(0)
        self.items.item_flow(2, 'BLACK')
        self.homepage.homepage_icon().click()
        self.homepage.headphones().click()
        self.categories.headphones_items(2)
        self.items.item_flow(3, 'YELLOW')
        self.cart.remove_item(0).click()
        '''Asserts that the item we removed is not in the cart, we chose index 0 because last item 
        we add will always be index 0 if we wanted to remove the tablet we would have to put index 1'''
        self.assertNotIn('HP H2310 IN-EAR HEADSET', self.cart.table_items())

    def test_4_fourth_task(self):
        '''This test tests that in the cart page, we see "shopping cart" in the top left of the page.'''
        self.homepage.tablets().click()
        self.categories.tablets_items(1)
        self.items.item_flow(1, 'GRAY')
        self.cart.cart_button().click()
        self.assertEqual(self.cart_page.shopping_cart_top_left(), 'SHOPPING CART')

    def test_5_fifth_task(self):
        '''Testing that the total price is according to the items prices and quantity'''
        self.homepage.speakers().click()
        self.categories.speakers_items(1)
        self.items.item_flow(6, 'TURQUOISE')
        first_product_sum = self.items.item_total_calculator()
        self.homepage.homepage_icon().click()
        self.homepage.mice().click()
        self.categories.mice_items(4)
        self.items.item_flow(2, 'GRAY')
        second_product_sum = self.items.item_total_calculator()
        self.homepage.homepage_icon().click()
        self.homepage.laptops().click()
        self.categories.laptops_items(6)
        self.items.item_flow(3, 'PURPLE')
        third_product_sum = self.items.item_total_calculator()
        self.cart.cart_button().click()
        self.assertEqual(self.cart_page.total_price(), self.items.format_returner(first_product_sum, second_product_sum, third_product_sum))
        print(f'First product name: {self.cart_page.product_name(0)} | Quantity:{self.cart_page.product_quantity(0)} | Price:{self.cart_page.product_price(0)}\n'
              f'Second product name: {self.cart_page.product_name(1)} | Quantity:{self.cart_page.product_quantity(1)} | Price:{self.cart_page.product_price(1)}\n'
              f'Third product name: {self.cart_page.product_name(2)} | Quantity:{self.cart_page.product_quantity(2)} | Price:{self.cart_page.product_price(2)}')



    def test_6_sixth_task(self):
        self.homepage.speakers().click()
        self.categories.speakers_items(0)
        self.items.item_flow(1, 'BLACK')
        self.homepage.homepage_icon().click()
        self.homepage.laptops().click()
        self.categories.laptops_items(0)
        self.items.item_flow(1, 'BLACK')
        self.cart.cart_button().click()
        self.cart_page.edit_button(0).click()
        self.items.change_quantity(4)
        self.items.add_to_cart().click()
        self.cart.cart_button().click()
        self.cart_page.edit_button(1).click()
        self.items.change_quantity(8)
        self.items.add_to_cart().click()
        self.cart.cart_button().click()
        self.assertEqual(self.cart_page.quantity(0), '4')
        self.assertEqual(self.cart_page.quantity(1), '8')
        '''Bug found when editing items inside cart page, second product never switches quantity,
         only the first product.'''

    def test_7_seventh_task(self):
        '''Testing that after entering tablet's item and pressing back,
         we indeed go back to the category of tablets, and after hitting back again we are in homepage'''
        self.homepage.tablets().click()
        self.categories.tablets_items(0)
        self.driver.back()
        # asserts that we are in tablets page
        self.assertEqual(self.driver.current_url, 'https://www.advantageonlineshopping.com/#/category/Tablets/3')
        self.driver.back()
        # asserts that we are in home page
        self.assertEqual(self.driver.current_url, 'https://www.advantageonlineshopping.com/#/')

    def test_8_eighth_task(self):
        self.homepage.mice().click()
        self.categories.mice_items(0)
        self.items.item_flow(1, 'BLACK')
        self.cart.checkout_button().click()
        self.registration.registration_button().click()
        self.registration.account_details('yanyan', '123123aA', '123123aA', '1@1.com')
        while True:
                self.registration.terms().click()
                break
        self.registration.register().click()
        self.checkout.next_button().click()
        self.checkout.safepay_flow('yanyaN123', 'ahksla2LKJ')
        self.assertEqual(self.driver.current_url, 'https://www.advantageonlineshopping.com/#/orderPayment')
        self.cart.small_cart_num_disappearance_wait()
        self.homepage.account_icon().click()
        self.homepage.my_orders().click()
        self.assertEqual(len(self.orders.order_number(0)), 10)
        self.cart.small_cart_num_disappearance_wait()
        self.assertEqual(self.cart.cart_total_items_from_nav(), '0')
        self.homepage.delete_account_flow()
        self.homepage.homepage_logo()


    def test_9_1_ninth_task_save_for_future_use_unchecked(self):
        self.homepage.laptops().click()
        self.categories.laptops_items(8)
        self.items.item_flow(1, 'GRAY')
        self.homepage.homepage_icon().click()
        self.homepage.mice().click()
        self.categories.mice_items(3)
        self.items.item_flow(1, 'PURPLE')
        self.cart.cart_button().click()
        self.cart_page.checkout_button().click()
        self.cart_page.sign_in_existing_acc_flow('catloverUNCHECK', '123123aA')
        self.checkout.next_button().click()
        self.checkout.master_credit_flow_uncheck_for_future_use('12345678912341234', '3423',
                                                                '07', '2025', 'firstname lastname')
        # Test fails because if save for future is not checked, payment wont go through.
        self.cart.small_cart_num_disappearance_wait()
        self.homepage.account_icon().click()
        self.homepage.my_orders().click()
        self.assertEqual(self.cart.cart_total_items_from_nav(), '0')
        self.assertEqual(len(self.orders.order_number(0)), 10)
        self.orders.delete_order().click()
        self.orders.delete_order_confirmation().click()

    def test_9_2_ninth_task_save_for_future_use_checked(self):
        self.homepage.laptops().click()
        self.categories.laptops_items(8)
        self.items.item_flow(1, 'GRAY')
        self.homepage.homepage_icon().click()
        self.homepage.mice().click()
        self.categories.mice_items(3)
        self.items.item_flow(1, 'PURPLE')
        self.cart.cart_button().click()
        self.cart_page.checkout_button().click()
        self.cart_page.sign_in_existing_acc_flow('catlover', '123123aA')
        self.checkout.next_button().click()
        self.checkout.master_credit_checkbox().click()
        self.checkout.edit_payment().click()
        self.checkout.master_credit_flow_future_use_checked('12345678912341234', '3423',
                                                            '07', '2025', 'firstname lastname')
        self.cart.small_cart_num_disappearance_wait()
        self.homepage.account_icon().click()
        self.homepage.my_orders().click()
        self.assertEqual(self.cart.cart_total_items_from_nav(), '0')
        self.assertEqual(len(self.orders.order_number(0)), 10)
        print(self.orders.order_number(0))
        self.orders.delete_order().click()
        self.orders.delete_order_confirmation().click()

    def test_tenth_task(self):
        '''Testing that both sign in and sign out are being done successfully.'''
        self.homepage.login_existing_user('catlover', '123123aA')
        self.assertEqual(self.homepage.username_proof(), 'catlover')
        
        self.homepage.log_out_flow()
        self.homepage.homepage_full_load()
        self.homepage.account_icon().click()
        self.homepage.sign_in_window_wait()
        self.assertEqual(self.homepage.sign_in_button().text, 'SIGN IN')
        self.homepage.exit_button().click()

    def tearDown(self):
        '''At end of each test, we are being moved to the Home Page, and then the test quits.'''
        self.homepage.homepage_icon().click()
        print(self.driver.current_url)
        self.driver.quit()
