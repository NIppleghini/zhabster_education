from selenium import webdriver

options = webdriver.EdgeOptions()
from selenium.webdriver.common.by import By
import pytest



@pytest.fixture()
def browser():
    browser = webdriver.Edge(options=options)
    browser.maximize_window()
    browser.implicitly_wait(60)
    yield browser
    browser.close()





def test_open_s6(browser):
	browser.get('https://www.demoblaze.com/')
	galaxy_s6 = browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
	galaxy_s6.click()
	title = browser.find_element(By.CSS_SELECTOR, value='h2')
	assert title.text == 'Samsung galaxy s6'
