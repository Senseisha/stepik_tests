import time
from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_have_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert button > 0, 'basket button not found'
