from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random


def print_stats(driver):
    print(driver.find_element_by_id("cookies").text)


def _list_numerated_elements_by_id(driver, name):
    elements = []
    ind = 0
    while True:
        try:
            elements.append(driver.find_element_by_id('{0}{1}'.format(name, ind)))
            ind += 1
        except:
            break
    return elements


def click_ups(driver):
    upgrades = _list_numerated_elements_by_id(driver, 'upgrade')
    products = _list_numerated_elements_by_id(driver, 'product')

    last_bad_product = len(products)
    last_bad_upgrade = len(upgrades)

    for i in range(5):
        if random.random() < 1/2:
            for ind in range(last_bad_product, -1, -1):
                try:
                    products[ind].click()
                except:
                    last_bad_product = ind
                    continue
        else:
            for ind in range(last_bad_upgrade, -1, -1):
                try:
                    upgrades[ind].click()
                except:
                    last_bad_upgrade = ind
                    continue


def refresh_info(driver):
    click_ups(driver)
    print_stats(driver)


def farm(driver, farm_time):
    while True:
        try:
            big_cookie = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'bigCookie')))
            big_cookie.click()
            break
        except:
            pass

    time_end = time.time() + farm_time
    next_refresh = 100
    while time.time() < time_end:
        big_cookie.click()
        next_refresh -= 1
        if next_refresh <= 0:
            refresh_info(driver)
            next_refresh = random.choice([i * 100 for i in range(1, 5)])
