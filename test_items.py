from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")


def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    btn = browser.find_element(*BTN_ADD_TO_BASKET)
    assert btn.is_displayed(), "Кнопка не видна"
    # sleep исключительно для удобства проверки работоспособности теста
    time.sleep(3)
