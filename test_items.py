import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_page_contains_button_put_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert button > 0, "Нельзя добавить в корзину"