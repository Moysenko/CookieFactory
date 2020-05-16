import browser
import clicker
import save_manager


def mine(farm_time, save_file, browser_name):
    with browser.CookieClickerSite(browser_name) as site:
        save_manager.load_from_save_file(site.driver, save_file)
        clicker.farm(site.driver, int(farm_time))
        save_manager.download_save_file(site.driver)
