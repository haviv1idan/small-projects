import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

website = "https://orteil.dashnet.org/cookieclicker/"
driver.get(website)
actions = ActionChains(driver)
big_cookie = driver.find_element(By.ID, "bigCookie")
cookies = driver.find_element(By.ID, "cookies")

time.sleep(2)
btn_got_it = driver.find_element(By.CLASS_NAME, "cc_btn.cc_btn_accept_all")
btn_got_it.click()

btn_x10 = driver.find_element(By.ID, "storeBulk10")
btn_x10.click()

while True:

    # close notifications
    try:
        close_notifications = driver.find_element(By.CLASS_NAME, "framed.close.sidenote")
        actions.click(close_notifications).perform()
    except NoSuchElementException:
        pass

    products = []
    big_cookie.click()

    # Finds upgrades
    upgrades = driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
    if upgrades:
        actions.click(upgrades[-1]).perform()
    else:
        # Find products
        products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
        products = [p for p in products if len(p.text) > 0]

        if products:
            actions.click(products[-1]).perform()

