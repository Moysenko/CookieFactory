from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
import glob


def _open_options(driver, attempts=10):
    for _ in range(attempts):
        try:
            options = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'prefsButton')))
            options.click()
            break
        except Exception:
            pass


def _get_save_name():
    return input('Name of file in input_saves with save:\n')


def load_from_save_file(driver, save_name):
    _open_options(driver)

    save_to_file_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'FileLoadInput')))
    save_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_saves',  save_name)
    save_to_file_button.send_keys(save_file)


def download_save_file(driver, download_attempts=10):
    output_saves_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_saves')
    for f in glob.glob(os.path.join(output_saves_dir, '*')):
        os.remove(f)

    for _ in range(download_attempts):
        try:
            print('Trying to save...')
            _open_options(driver)
            print('Options opened')
            save_to_file = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Save to file')))
            print('Found "Save to file" button')
            save_to_file.click()
            print('Download started...')
            break
        except Exception:
            print('Failed\n')
            pass

    while not glob.glob(output_saves_dir + '/*.txt'):
        time.sleep(1)

    os.rename(glob.glob(output_saves_dir + '/*.txt')[0], output_saves_dir + '/save.txt')

    print('Download finished!')
