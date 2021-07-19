from selenium.webdriver.chrome.webdriver import WebDriver
def test_onlinesim_ru ():
    driver = WebDriver(executable_path='/usr/bin/chromedriver')
    driver.get('https://onlinesim.ru/')
    search_button_buy_number = driver.find_element_by_xpath('//a[@title="Купить номер"]')
    search_button_buy_number.click()


