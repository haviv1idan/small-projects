from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

website = "https://orteil.dashnet.org/cookieclicker/"
driver.get(website)
actions = ActionChains(driver)
big_cookie = driver.find_element(By.ID, "bigCookie")
cookies = driver.find_element(By.ID, "cookies")


while True:
    products = []
    # actions.move_to_element(big_cookie).click(big_cookie).perform()
    big_cookie.click()
    int_cookies = int(cookies.text.split()[0].replace(',', ''))

    # Finds upgrades
    upgrades = driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
    for i, upgrade in enumerate(upgrades[::-1]):
        print("index: {}, upgrade: {}".format(i, upgrade.text))
        actions.click(upgrade).perform()
        # upgrade.click()
        int_cookies = int(cookies.text.split()[0].replace(',', ''))

    print("cookies: ", int_cookies)
    # Find products
    products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
    products = [p for p in products if len(p.text) > 0]

    if products and int_cookies < int(products[-1].text.split()[1].replace(',', '')):
        continue
    else:
        for i, product in enumerate(products[::-1]):
            print("index: {}, product: {}".format(i, product.text))
            actions.click(product).perform()
            # product.click()
            break
