from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
import random

cur_dir = os.path.dirname(os.path.abspath(__file__)) + '/saves'
driver = None


def _open_site():
    global driver
    chrome_options = webdriver.ChromeOptions()
    preference = {'download.default_directory': cur_dir,
                  "safebrowsing.enabled": "false"}
    chrome_options.add_experimental_option('prefs', preference)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    driver.get('https://orteil.dashnet.org/cookieclicker/')


def click_ups():
    upgrades = []
    ind = 0
    while True:
        try:
            upgrades.append(driver.find_element_by_id(f'upgrade{ind}'))
            ind += 1
        except:
            break

    products = []
    ind = 0
    while True:
        try:
            products.append(driver.find_element_by_id(f'product{ind}'))
            ind += 1
        except:
            break

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


def _farm(farm_time):
    while True:
        try:
            bigCookie = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'bigCookie')))
            bigCookie.click()
            break
        except:
            pass

    time_end = time.time() + farm_time
    next_time_update = 100
    while time.time() < time_end:
        bigCookie.click()
        next_time_update -= 1
        if next_time_update <= 0:
            click_ups()
            next_time_update = random.choice([i * 100 for i in range(1, 5)])


def _save():
    while True:
        try:
            options = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="prefsButton"]')))
            options.click()
            break
        except:
            pass

    save_to_file = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu"]/div[3]/div[4]/a[1]')))
    save_to_file.click()

    while len(os.listdir(cur_dir)) == 0:
        time.sleep(1)

    driver.quit()


def main():
    _open_site()
    farm_time = 600
    _farm(farm_time)
    _save()


main()
