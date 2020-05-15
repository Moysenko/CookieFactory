import unittest
import browser
import save_manager
import timeout_decorator
import clicker
import os


class TestBrowser(unittest.TestCase):

    @timeout_decorator.timeout(50)
    def test_open_and_close(self):
        site = browser.CookieClickerSite()
        try:
            site.__enter__()
        except Exception:
            self.fail("site.open() raised Exception unexpectedly!")

        try:
            site.__exit__()
        except Exception:
            self.fail("site.close() raised Exception unexpectedly!")


class TestSaveManager(unittest.TestCase):

    @timeout_decorator.timeout(50)
    def test_open_options(self):
        with browser.CookieClickerSite() as site:
            try:
                save_manager._open_options(site.driver)
            except Exception:
                self.fail("_open_options() raised Exception unexpectedly!")

    @timeout_decorator.timeout(50)
    def test_load_from_save_file(self):
        with browser.CookieClickerSite() as site:
            try:
                save_manager.load_from_save_file(site.driver, 'test.txt')
            except Exception:
                self.fail("load_from_save_file() raised Exception unexpectedly!")

    @timeout_decorator.timeout(50)
    def test_download_save_file(self):
        with browser.CookieClickerSite() as site:
            try:
                save_manager.download_save_file(site.driver)
            except Exception:
                self.fail("download_save_file() raised Exception unexpectedly!")

    @timeout_decorator.timeout(50)
    def test_downloaded_file_exists(self):
        with browser.CookieClickerSite() as site:
            try:
                save_manager.download_save_file(site.driver)
                self.assertTrue(os.path.isfile(
                    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_saves', 'save.txt')))
            except Exception:
                self.fail("download_save_file() raised Exception unexpectedly!")


class TestClicker(unittest.TestCase):

    @timeout_decorator.timeout(120)
    def test_click_ups(self):
        with browser.CookieClickerSite() as site:
            try:
                clicker.click_ups(site.driver)
            except Exception:
                self.fail("click_ups() raised Exception unexpectedly!")

    @timeout_decorator.timeout(120)
    def test_print_stats(self):
        with browser.CookieClickerSite() as site:
            try:
                clicker.get_stats(site.driver)
            except Exception:
                self.fail("print_stats() raised Exception unexpectedly!")

    @timeout_decorator.timeout(120)
    def test_farm(self):
        with browser.CookieClickerSite() as site:
            try:
                clicker.farm(site.driver, 30)
            except Exception:
                self.fail("farm() raised Exception unexpectedly!")

    @timeout_decorator.timeout(120)
    def test_clicks_are_working(self):
        with browser.CookieClickerSite() as site:
            try:
                clicker.farm(site.driver, 30)
                before = clicker.get_stats(site.driver)
                clicker.farm(site.driver, 30)
                after = clicker.get_stats(site.driver)
                self.assertNotEqual(before, after)
            except Exception:
                self.fail("farm() raised Exception unexpectedly!")


class TestClickerAndSaveManager(unittest.TestCase):

    @timeout_decorator.timeout(120)
    def test_loading_is_working(self):
        with browser.CookieClickerSite() as site:
            try:
                clicker.farm(site.driver, 10)
                before = clicker.get_stats(site.driver)
                save_manager.load_from_save_file(site.driver, 'test.txt')
                clicker.farm(site.driver, 2)
                after = clicker.get_stats(site.driver)
                self.assertNotEqual(before, after)
            except Exception:
                self.fail("farm() raised Exception unexpectedly!")
