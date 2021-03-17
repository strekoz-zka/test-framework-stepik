# import time
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    # time.sleep(10)
    browser.implicitly_wait(5)
    try:
        basket_button = browser.find_element_by_css_selector('button[class*="add-to-basket"]')
    except NoSuchElementException:
        basket_button = None
    assert basket_button is not None, "No basket button"
