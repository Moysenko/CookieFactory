import browser
import clicker
import save_manager


def _get_farm_time():
    return int(input('Time in seconds to farm:\n'))


def mine(farm_time, saveFile):
    site = browser.Site()
    site.open()
    save_manager.load_from_save_file(site.driver, saveFile)
    clicker.farm(site.driver, int(farm_time))
    save_manager.download_save_file(site.driver)
    site.close()
