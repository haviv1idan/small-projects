from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

website = "https://orteil.dashnet.org/cookieclicker/"
driver.get(website)
actions = ActionChains(driver)
big_cookie = driver.find_element(By.ID, "bigCookie")
cookies = driver.find_element(By.ID, "cookies")


while True:

    # close notifications
    try:
        close_notifications = driver.find_element(By.CLASS_NAME, "framed.close.sidenote")
        print(close_notifications)
        actions.click(close_notifications).perform()
    except NoSuchElementException:
        pass

    products = []
    big_cookie.click()
    int_cookies = int(cookies.text.split()[0].replace(',', ''))

    # Finds upgrades
    upgrades = driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
    for i, upgrade in enumerate(upgrades[::-1]):
        # print("index: {}, upgrade: {}".format(i, upgrade.text))
        # upgrade.click()
        actions.click(upgrade).perform()
        int_cookies = int(cookies.text.split()[0].replace(',', ''))

    # print("cookies: ", int_cookies)
    # Find products
    products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
    products = [p for p in products if len(p.text) > 0]

    if products and int_cookies < int(products[-1].text.split()[1].replace(',', '')):
        continue
    else:
        for i, product in enumerate(products[::-1]):
            # print("index: {}, product: {}".format(i, product.text))
            # product.click()
            actions.click(product).perform()
            break
