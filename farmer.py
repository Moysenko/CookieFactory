from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
import random
import glob

cur_dir = os.path.dirname(os.path.abspath(__file__))
driver = None


def _open_site():
    global driver
    chrome_options = webdriver.ChromeOptions()
    preference = {'download.default_directory': os.path.join(cur_dir, 'output_saves'),
                  "safebrowsing.enabled": "false"}
    chrome_options.add_experimental_option('prefs', preference)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    driver.get('https://orteil.dashnet.org/cookieclicker/')


def print_stats():
    print(driver.find_element_by_id("cookies").text)


def list_numerated_elements_by_id(name):
    elements = []
    ind = 0
    while True:
        try:
            elements.append(driver.find_element_by_id('{0}{1}'.format(name, ind)))
            ind += 1
        except:
            break
    return elements


def click_ups():
    upgrades = list_numerated_elements_by_id('upgrade')
    products = list_numerated_elements_by_id('product')

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


def refresh_info():
    click_ups()
    print_stats()


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
    next_refresh = 100
    while time.time() < time_end:
        bigCookie.click()
        next_refresh -= 1
        if next_refresh <= 0:
            refresh_info()
            next_refresh = random.choice([i * 100 for i in range(1, 5)])


def _open_options():
    while True:
        try:
            options = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'prefsButton')))
            options.click()
            break
        except:
            pass


def _save():
    output_saves_dir = os.path.join(cur_dir, 'output_saves')
    for f in glob.glob(os.path.join(output_saves_dir, '*')):
        os.remove(f)

    _open_options()

    save_to_file = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Save to file')))
    save_to_file.click()

    while not os.listdir(output_saves_dir):
        time.sleep(1)

    driver.quit()


def _get_farm_time():
    return int(input('Time in seconds to farm: '))


def _get_save_name():
    return input('Name of file in input_saves with save: ')


def _open_save():
    save_name = _get_save_name()
    if not save_name:
        return

    _open_options()

    save_to_file_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'FileLoadInput')))
    save_file = os.path.join(cur_dir, 'input_saves',  save_name)
    save_to_file_button.send_keys(save_file)


def main():
    _open_site()
    _open_save()
    farm_time = _get_farm_time()
    _farm(farm_time)
    _save()


main()
