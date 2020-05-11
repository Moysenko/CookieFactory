import browser
import farmer
import save_manager


def _get_farm_time():
    return int(input('Time in seconds to farm:\n'))


def main():
    site = browser.Site()
    site.open()
    save_manager.load_from_save_file(site.driver)
    farm_time = _get_farm_time()
    farmer.farm(site.driver, farm_time)
    save_manager.download_save_file(site.driver)
    site.close()


main()