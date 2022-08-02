from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
from booking.booking_filtration import BookingFiltration



class Booking(webdriver.Chrome):  #the main Class in the project inherited from webdriver.Chrome class
    def __init__(self, driver_path=r'C:\Users\t90na\Downloads\chromedriver_win32', teardown = True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path   # always add the driver path to the environment variables
        super().__init__()
        self.implicitly_wait(30)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()  #this with shut down the browser after all commends inside "with" finishes.

    #change currency
    def choose_your_currency(self, currency = 'USD'):
        currency_element = self.find_element_by_css_selector(
            'button,[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        new_currency = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={currency}&top_currency=1"]'
        )
        new_currency.click()

    #select where to go
    def choose_your_destination(self, place_to_go):
        dest = self.find_element_by_id("ss")
        dest.clear()   #clean search bar
        dest.send_keys(place_to_go)
        my_dest = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        my_dest.click()

    #select check-in and check-out dates in the format of 'yyyy-mm-dd'
    def select_dates(self, checkin_date, checkout_date):
        checkin_element = self.find_element_by_css_selector(
            f'td[data-date="{checkin_date}"]'
        )
        checkin_element.click()

        checkout_element = self.find_element_by_css_selector(
            f'td[data-date="{checkout_date}"]'
        )
        checkout_element.click()

    #specify number of adults
    def how_many_adults(self, count=2):
        adults = self.find_element_by_id("xp__guests__toggle")
        adults.click()
        while True:
            decrease_adults_element = self.find_element_by_css_selector('button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()

            adults_value_element = self.find_element_by_id("group_adults")
            adults_value = adults_value_element.get_attribute('value')  #returns the adults count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        for i in range(count-1):
            increase_button_element.click()

        search = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search.click()


    #filtering results
    def apply_Filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)   # filtering according to star rating
        filtration.sort_price_lowest_first()  #filtering according to lowest price.


