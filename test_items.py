from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(*BTN_ADD_TO_BASKET)
    # sleep исключительно для удобства проверки работоспособности теста
    time.sleep(3)
