import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_exist(browser):
    browser.get(link)
    basket_button = browser.find_element_by_class_name('btn-add-to-basket')
    assert basket_button.is_displayed(), 'Add-to-basket button is not displayed'
