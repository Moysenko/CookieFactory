from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os


class Site:
    def open(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        print("Headless Chrome Initialized")
        params = {'behavior': 'allow', 'downloadPath': os.path.dirname(os.path.abspath(__file__)) + '/output_saves'}
        self.driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
        self.driver.get('https://orteil.dashnet.org/cookieclicker/')

    def close(self):
        self.driver.quit()
