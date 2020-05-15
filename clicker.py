from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
import save_manager


def get_stats(driver):
    return driver.find_element_by_id("cookies").text


def _list_numerated_elements_by_id(driver, name, attempts=10):
    elements = []
    ind = 0
    for _ in range(attempts):
        try:
            elements.append(driver.find_element_by_id('{0}{1}'.format(name, ind)))
            ind += 1
        except Exception:
            break
    return elements


def try_click_list(clickable_list):
    for ind in range(len(clickable_list) - 1, -1, -1):
        try:
            clickable_list[ind].click()
        except Exception:
            clickable_list.pop(ind)
            continue


def click_ups(driver, update_attempts=5):
    upgrades = _list_numerated_elements_by_id(driver, 'upgrade')
    products = _list_numerated_elements_by_id(driver, 'product')

    for _ in range(update_attempts):
        if random.random() < 0.5:
            try_click_list(upgrades)
        else:
            try_click_list(products)


def _print_border():
    print('-' * 20)


def refresh_info(driver):
    _print_border()
    print('Stats before upgrades:\n', get_stats(driver))
    click_ups(driver)
    print('Stats after upgrades:\n', get_stats(driver))
    _print_border()


def get_cookie(driver, attempts=10):
    for _ in range(attempts):
        try:
            big_cookie = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'bigCookie')))
            big_cookie.click()
            return big_cookie
        except Exception:
            pass
    assert False, "Big Cookie "


def farm(driver, farm_time):
    big_cookie = get_cookie(driver)

    time_end = time.time() + farm_time
    next_refresh = 100
    next_save = 50000
    while time.time() < time_end:
        driver.execute_script('arguments[0].click();', big_cookie)
        next_refresh -= 1
        next_save -= 1
        if next_refresh <= 0:
            refresh_info(driver)
            next_refresh = random.randint(10, 30) * 1000
            print("Next refresh in {0} clicks".format(next_refresh))
        if next_save <= 0:
            save_manager.download_save_file(driver)
            next_save = 50000
