#this file will include a class with instance method that
#will be responsible to interact with our website
#after we have some results, to apply filtration


#use this to ensure autocomplition
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver:WebDriver ):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        all_filters = self.driver.find_element_by_css_selector(
            'div[data-testid="filters-sidebar"]'
        )
        star_filtration_box = all_filters.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')  #gives all child elements
        print(len(star_child_elements))
        for star_value in star_values:
            for star_element in star_child_elements:
               if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        element.click()


