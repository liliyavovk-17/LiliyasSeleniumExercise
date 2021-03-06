from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class BasePage(object):
    '''Base class to initialize the base page that will be called from all pages.'''

    def __init__(self, driver):
        self.driver = driver



    # def await_traits(self):
    #     '''
    #     Checks the all the elements in self.traits array exist in the DOM.
    #     Used to ensure we are on the desired page with the necessary elements loaded.
    #     Returns self.
    #     '''
    #     for locator in self.traits:
    #         self.driver.find_element(*locator)
    #     return self


# class BasePageElement(object):
#     """Base page class that is initialized on every page object class."""

#     def __set__(self, obj, value):
#         """Sets the text to the value supplied."""
#         driver = obj.driver
#         WebDriverWait(driver, 10).until(
#             lambda driver: driver.find_element(*self.locator))
#         driver.find_element(*self.locator).send_keys(value)

#     def __get__(self, obj, owner):
#         """Gets the text of the specified object."""
#         driver = obj.driver
#         WebDriverWait(driver, 10).until(
#             lambda driver: driver.find_element(*self.locator))
#         element = driver.find_element(*self.locator)
#         return element.get_attribute("value")
