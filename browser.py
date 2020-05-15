from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import os


class BrowserDriver:
    def __init__(self, browser_name="Headless Chrome"):
        if browser_name == "Headless Chrome":
            self.init_headless_chrome()
        elif browser_name == "Chrome":
            self.init_chrome()
        elif browser_name == "Firefox":
            self.init_firefox()
        else:
            assert False, "Unexpected browser name"

    def init_headless_chrome(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        print("Headless Chrome Initialized")
        params = {'behavior': 'allow', 'downloadPath': os.path.dirname(os.path.abspath(__file__)) + '/output_saves'}
        self.driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

    def init_chrome(self):
        options = webdriver.ChromeOptions()
        download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_saves')
        preference = {'download.default_directory': download_path, "safebrowsing.enabled": "false"}
        options.add_experimental_option('prefs', preference)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    def init_firefox(self):
        profile = webdriver.FirefoxProfile()
        profile.headless = True
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_saves')
        profile.set_preference("browser.download.dir", download_path)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)


class CookieClickerSite(BrowserDriver):
    def __enter__(self):
        self.driver.get('https://orteil.dashnet.org/cookieclicker/')
        return self

    def __exit__(self, *args):
        self.driver.quit()
        return False
