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
        self.driver.get("http://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        # We chose high number because the site experiences high loads very often
        self.driver.implicitly_wait(50)
        # Creating all the necessary objects for the test
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
        # Click on the mice category from homepage
        self.categories.mice_items(0)
        # Click on the first item in the mice category
        self.items.item_flow(2, 'BLACK')
        # Choosing quantity of 2, with the color BLACK
        self.homepage.homepage_icon().click()
        # Go back to the homepage
        self.homepage.speakers().click()
        # Click on the speakers category from homepage
        self.categories.speakers_items(0)
        # Click on the first item in the mice category
        self.items.item_flow(3, 'GRAY')
        # Choosing quantity of 3, with the color Gray
        self.assertEqual(self.cart.cart_total_items_from_nav(), '5')
        # asserts that the total number of items in the cart is 5, 3+2

    def test_2_second_task(self):
        '''This test verifies that each product we add to the cart
         matches the correct name, color, price and quantity.'''
        # ==============================FIRST PRODUCT====================================
        self.homepage.mice().click()
        # Click on the mice category from homepage
        self.categories.mice_items(3)
        # Click on the first item in the mice category
        self.items.item_flow(2, 'RED')
        # Choosing quantity of 2, with the color BLACK
        '''Asserting that the color, name, quantity and price are as expected'''
        self.assertEqual(self.cart.cart_product_color(0), 'RED')
        self.assertEqual(self.cart.cart_product_name(0), 'HP Z4000 WIRELESS MOUSE')
        self.assertEqual(self.cart.cart_product_quantity(0), 'QTY: 2')
        self.assertEqual(self.cart.cart_product_price(0), self.cart.price_calculator(0))
        self.homepage.homepage_icon().click()
        # Go to the homepage
        # ==============================SECOND PRODUCT====================================
        self.homepage.speakers().click()
        # Click on the speakers category from homepage
        self.categories.speakers_items(0)
        # Click on the first item in the speakers category
        self.items.item_flow(3, 'GRAY')
        # Choosing quantity of 3, with the color Gray
        '''Asserting that the color, name, quantity and price are as expected'''
        self.assertEqual(self.cart.cart_product_color(0), 'GRAY')
        self.assertEqual(self.cart.cart_product_color(1), 'RED')
        '''The elements are being stacked instead of being in a certain order, index 0 will
         always be the latest added product, test above proves it'''
        self.assertIn('BOSE SOUNDLINK BLUETOOTH', self.cart.cart_product_name(0))
        self.assertEqual(self.cart.cart_product_quantity(0), 'QTY: 3')
        self.assertEqual(self.cart.cart_product_price(0), self.cart.price_calculator(0))
        self.homepage.homepage_icon().click()
        # Go to the homepage
        # ==============================THIRD PRODUCT====================================
        self.homepage.tablets().click()
        # Click on the tablets category from homepage
        self.categories.tablets_items(0)
        # Click on the first item in the tablets category
        self.items.item_flow(4, 'BLACK')
        # Choosing quantity of 4, with the color Black
        '''Asserting that the color, name, quantity and price are as expected'''
        self.assertEqual(self.cart.cart_product_color(0), 'BLACK')
        self.assertIn('HP ELITEPAD 1000 G2 TABLET', self.cart.cart_product_name(0))
        self.assertEqual(self.cart.cart_product_quantity(0), 'QTY: 4')
        self.assertIn(self.cart.price_calculator(0), self.cart.cart_product_price(0))
        '''Bug found, when choosing HP elitepad color black, it shows as color BLUE in the cart.'''

    def test_3_third_task(self):
        '''Testing the functionality of the "X" button in cart hover menu'''
        self.homepage.tablets().click()
        # Click on the tablets category from homepage
        self.categories.tablets_items(0)
        # Click on the first item in the tablets category
        self.items.item_flow(2, 'BLACK')
        # Choosing quantity of 2, with the color Black
        self.homepage.homepage_icon().click()
        # Go to the homepage
        self.homepage.headphones().click()
        # Click on the headphones category from homepage
        self.categories.headphones_items(2)
        # Click on the third item in the headphones category
        self.items.item_flow(3, 'YELLOW')
        # Choosing quantity of 3, with the color Yellow
        self.cart.remove_item(0).click()
        # Removing the last item we added to the cart
        '''Asserts that the item we removed is not in the cart, we chose index 0 because last item 
        we add will always be index 0 if we wanted to remove the tablet we would have to put index 1'''
        self.assertNotIn('HP H2310 IN-EAR HEADSET', self.cart.table_items())

    def test_4_fourth_task(self):
        '''This test tests that in the cart page, we see "shopping cart" in the top left of the page.'''
        self.homepage.tablets().click()
        # Click on the tablets category from homepage
        self.categories.tablets_items(1)
        # Click on the second item in the tablets category
        self.items.item_flow(1, 'GRAY')
        # Choosing quantity of 1, with the color Gray
        self.cart.cart_button().click()
        # Click on the cart icon, proceed to cart page
        self.assertEqual(self.cart_page.shopping_cart_top_left(), 'SHOPPING CART')
        # Assert that there is 'shopping cart' at the top left of the screen.

    def test_5_fifth_task(self):
        '''Testing that the total price is according to the items prices and quantity'''
        self.homepage.speakers().click()
        # Click on the speakers category from homepage
        self.categories.speakers_items(1)
        # Click on the second item in the speakers category
        self.items.item_flow(6, 'TURQUOISE')
        # Choosing quantity of 6, with the color Turquoise
        first_product_sum = self.items.item_total_calculator()
        # Setting a variable for the first product price X quantity
        self.homepage.homepage_icon().click()
        # Go to the homepage
        self.homepage.mice().click()
        # Click on the mice category from homepage
        self.categories.mice_items(4)
        # Click on the fifth item in the speakers category
        self.items.item_flow(2, 'GRAY')
        # Choosing quantity of 2, with the color Gray
        second_product_sum = self.items.item_total_calculator()
        # Setting a variable for the second product price X quantity
        self.homepage.homepage_icon().click()
        # Go to the homepage
        self.homepage.laptops().click()
        # Click on the laptops category from homepage
        self.categories.laptops_items(6)
        # Click on the seventh item in the speakers category
        self.items.item_flow(3, 'PURPLE')
        # Choosing quantity of 3, with the color Purple
        third_product_sum = self.items.item_total_calculator()
        # Setting a variable for the third product price X quantity
        self.cart.cart_button().click()
        # Click on the cart logo, proceed to cart page
        self.assertEqual(self.cart_page.total_price(), self.items.format_returner(first_product_sum, second_product_sum, third_product_sum))
        # Assert that the sum of the three variables equals to the total price in the cart page
        print(f'First product name: {self.cart_page.product_name(2)} | Quantity:{self.cart_page.product_quantity(2)} | Price:{self.cart_page.product_price(2)}\n'
              f'Second product name: {self.cart_page.product_name(1)} | Quantity:{self.cart_page.product_quantity(1)} | Price:{self.cart_page.product_price(1)}\n'
              f'Third product name: {self.cart_page.product_name(0)} | Quantity:{self.cart_page.product_quantity(0)} | Price:{self.cart_page.product_price(0)}')
        # Print each product name, quantity and price

    def test_6_sixth_task(self):
        '''This test checks that after choosing 2 different products, and editing their quantity through the cart page,
        the changes are saved successfully.'''
        self.homepage.speakers().click()
        # Click on speakers category from homepage
        self.categories.speakers_items(0)
        # Choosing first item from speakers category
        self.items.item_flow(1, 'BLACK')
        # Quantity 1, Color Black
        self.homepage.homepage_icon().click()
        # Go to Homepage
        self.homepage.laptops().click()
        # Click on laptops category from homepage
        self.categories.laptops_items(0)
        # Choosing first item from latops category
        self.items.item_flow(1, 'BLACK')
        # Quantity 1, Color Black
        self.cart.cart_button().click()
        # Click on cart icon, proceed to cart page
        self.cart_page.edit_button(0).click()
        # Click edit on the first product in the cart page
        self.items.change_quantity(4)
        # Change the quantity to 4
        self.items.add_to_cart().click()
        # Add the product to the cart after quantity change
        self.cart.cart_button().click()
        # Go again to cart page
        self.cart_page.edit_button(1).click()
        # Click edit on the second product in the cart page
        self.items.change_quantity(8)
        # Change the quantity to 8
        self.items.add_to_cart().click()
        # Add the product to the cart after quantity change
        self.cart.cart_button().click()
        # Go again to cart page
        self.assertEqual(self.cart_page.quantity(0), '4')
        # Asserting that the first product quantity is 4
        self.assertEqual(self.cart_page.quantity(1), '8')
        # Asserting that the second product quantity is 8
        '''Bug found when editing items inside cart page, second product never switches quantity,
         only the first product.'''

    def test_7_seventh_task(self):
        '''Testing that after entering tablet's item and pressing back,
         we indeed go back to the category of tablets, and after hitting back again we are in homepage'''
        self.homepage.tablets().click()
        # Click on tablets category from homepage
        self.categories.tablets_items(0)
        # Click on the first product in tablet category
        self.driver.back()
        # Go back
        self.assertEqual(self.driver.current_url, 'http://www.advantageonlineshopping.com/#/category/Tablets/3')
        # asserts that we are in tablets page
        self.driver.back()
        # Go back
        self.assertEqual(self.driver.current_url, 'http://www.advantageonlineshopping.com/#/')
        # asserts that we are in home page

    def test_8_eighth_task(self):
        '''This test checks that checkout process with new user using safepay is done successfully,
        checks that payment is successful, and the total items in the cart resets to zero, and
        the order appears in "My Orders" page.'''
        self.homepage.mice().click()
        # Click on mice category from homepage
        self.categories.mice_items(0)
        # Click on the first product in mice category
        self.items.item_flow(1, 'BLACK')
        # Quantity 1, Color Black
        self.cart.checkout_button().click()
        # Click on checkout in the cart window
        self.registration.registration_button().click()
        # Click on "Registration"
        self.registration.account_details('yanyan', '123123aA', '123123aA', '1@1.com')
        # Fill the fields with the proper details
        self.registration.terms().click()
        # Click on accept terms
        self.registration.register().click()
        # Click on register
        self.checkout.next_button().click()
        # Click on next
        self.checkout.safepay_flow('yanyaN123', 'ahksla2LKJ')
        # Enter safepay credentials
        self.checkout.wait_for_payment_success_window()
        # Waits until payment success window appears
        self.assertEqual(self.driver.current_url, 'http://www.advantageonlineshopping.com/#/orderPayment')
        # Assert that the current url is the order payment invoice, checks that payment is successful
        order_checkout_order_number = self.checkout.order_number_from_completion_page()
        # We put a variable that takes the order number
        self.cart.small_cart_num_disappearance_wait()
        # Waits until the small number in cart disappears, and only then continues
        self.homepage.account_icon().click()
        # Click on account icon in the nav
        self.homepage.my_orders().click()
        # Click on my orders
        self.assertEqual(self.orders.order_number(-1), order_checkout_order_number)
        # Assert that the order number from the payment successful page matches
        # The order number in my orders page.
        self.cart.small_cart_num_disappearance_wait()
        # Waits until the small number in cart disappears, and only then continues
        self.assertEqual(self.cart.cart_total_items_from_nav(), '0')
        # Assert that the total items in the cart is 0 in the window page
        self.homepage.delete_account_flow()
        # Flow for deleting the account so we dont need to create a new one each test
        self.homepage.wait_until_pop_up_goes_away()
        # Waits until the delete confirmation pop up window goes away

    def test_9_1_ninth_task_save_for_future_use_unchecked(self):
        '''This test checks that checkout process with existing user using master credit is done successfully,
        and the total items in the cart resets to zero, and the order appears in "My Orders" page.
        This test checks the checkout without saving the credit card for future use'''
        self.homepage.laptops().click()
        # Click on laptops category from homepage
        self.categories.laptops_items(8)
        # Click on the ninth laptop product
        self.items.item_flow(1, 'GRAY')
        # Add it to the cart with quantity of 1, color Gray
        self.homepage.homepage_icon().click()
        # Go to the home page
        self.homepage.mice().click()
        # Click on mice category from homepage
        self.categories.mice_items(3)
        # Click on the fourth mice product
        self.items.item_flow(1, 'PURPLE')
        # Add it to the cart with quantity of 1, color purple
        self.cart.cart_button().click()
        # Click on the cart icon, proceed to cart page
        self.cart_page.checkout_button().click()
        # Click on checkout in the bottom of the page
        self.cart_page.sign_in_existing_acc_flow('catloverUNCHECK', '123123aA')
        # Enter existing user credentials, and click sign in
        self.checkout.next_button().click()
        # Click on next button
        self.checkout.master_credit_flow_uncheck_for_future_use('12345678912341234', '423',
                                                                '07', '2025', 'firstname lastname')
        # Enter the master credit credentials WITHOHUT checking the save for future option
        # Test fails because if save for future is not checked, payment wont go through.
        self.checkout.wait_for_payment_success_window()
        # Waits until payment success window appears
        order_checkout_order_number = self.checkout.order_number_from_completion_page()
        # We put a variable that takes the order number
        self.cart.small_cart_num_disappearance_wait()
        # Waits until the small number in cart disappears, and only then continues
        self.homepage.account_icon().click()
        # Click on the account icon
        self.homepage.my_orders().click()
        # Click on "My orders"
        self.assertEqual(self.cart.cart_total_items_from_nav(), '0')
        # Assert that the total items in the cart is 0 in the window page
        self.assertEqual(self.orders.order_number(-1), order_checkout_order_number)
        # Assert that the order number from the payment successful page matches
        # The order number in my orders page.
        self.orders.delete_order(-1).click()
        # Delete the most recent order from "my orders" page
        self.orders.delete_order_confirmation().click()
        # Click Yes in delete order confirmation

    def test_9_2_ninth_task_save_for_future_use_checked(self):
        '''This test checks that checkout process with existing user using master credit is done successfully,
        and the total items in the cart resets to zero, and the order appears in "My Orders" page.
        This test checks the checkout with saving the credit card for future use'''
        self.homepage.laptops().click()
        # Click on laptops category from homepage
        self.categories.laptops_items(8)
        # Click on the ninth laptop product
        self.items.item_flow(1, 'GRAY')
        # Add it to the cart with quantity of 1, color Gray
        self.homepage.homepage_icon().click()
        # Go to the home page
        self.homepage.mice().click()
        # Click on mice category from homepage
        self.categories.mice_items(3)
        # Click on the fourth mice product
        self.items.item_flow(1, 'PURPLE')
        # Add it to the cart with quantity of 1, color purple
        self.cart.cart_button().click()
        # Click on the cart icon, proceed to cart page
        self.cart_page.checkout_button().click()
        # Click on checkout in the bottom of the page
        self.cart_page.sign_in_existing_acc_flow('catlover', '123123aA')
        # Enter existing user credentials, and click sign in
        self.checkout.next_button().click()
        # Click on next button
        self.checkout.master_credit_checkbox().click()
        # Click on master credit checkbox
        self.checkout.edit_payment().click()
        # Click on edit payment information
        self.checkout.master_credit_flow_future_use_checked('12345678912341234', '423',
                                                            '07', '2025', 'firstname lastname')
        # Enter the master credit credentials WITH checking the save for future option
        self.checkout.wait_for_payment_success_window()
        # Waits until payment success window appears
        order_checkout_order_number = self.checkout.order_number_from_completion_page()
        # We put a variable that takes the order number
        self.cart.small_cart_num_disappearance_wait()
        # Waits until the small number in cart disappears, and only then continues
        self.homepage.account_icon().click()
        # Click on the account icon
        self.homepage.my_orders().click()
        # Click on "My orders"
        self.assertEqual(self.cart.cart_total_items_from_nav(), '0')
        # Assert that the total items in the cart is 0 in the window page
        self.assertEqual(self.orders.order_number(-1), order_checkout_order_number)
        # Assert that the order number from the payment successful page matches
        # The order number in my orders page.
        self.orders.delete_order(-1).click()
        # Delete the most recent order from "my orders" page
        self.orders.delete_order_confirmation().click()
        # Click Yes in delete order confirmation

    def test_tenth_task(self):
        '''Testing that both sign in and sign out are being done successfully.'''
        self.homepage.login_existing_user('catlover', '123123aA')
        # Click on account icon, add the existing username and password and click on log-in
        self.assertEqual(self.homepage.username_proof(), 'catlover')
        # Assert that the current username is: catlover
        self.homepage.log_out_flow()
        # Click on account icon, click on logout
        self.homepage.homepage_full_load()
        # Waits until the page is fully loaded
        self.homepage.account_icon().click()
        # Click on account icon
        self.homepage.sign_in_window_wait()
        # Wait until the pop-up window appears
        self.assertEqual(self.homepage.sign_in_button().text, 'SIGN IN')
        # Assert that 'Sign in' exists in the pop-up window, proves that we are not logged-in
        self.homepage.exit_button().click()
        # Click on the "X" button in the pop-up window

    def tearDown(self):
        '''At end of each test, we are being moved to the Home Page, and then the test quits.'''
        self.homepage.homepage_icon().click()
        print(self.driver.current_url)
        self.driver.quit()
