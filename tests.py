import unittest
import browser
import save_manager
import timeout_decorator
import clicker


class TestBrowser(unittest.TestCase):

    @timeout_decorator.timeout(50)
    def test_open_and_close(self):
        site = browser.Site()
        try:
            site.open()
        except Exception:
            self.fail("site.open() raised Exception unexpectedly!")

        try:
            site.close()
        except Exception:
            self.fail("site.close() raised Exception unexpectedly!")


class TestSaveManager(unittest.TestCase):

    @timeout_decorator.timeout(50)
    def test_open_options(self):
        site = browser.Site()
        site.open()
        try:
            save_manager._open_options(site.driver)
        except Exception:
            self.fail("_open_options() raised Exception unexpectedly!")
        site.close()

    @timeout_decorator.timeout(50)
    def test_load_from_save_file(self):
        site = browser.Site()
        site.open()
        try:
            save_manager.load_from_save_file(site.driver, 'test.txt')
        except Exception:
            self.fail("load_from_save_file() raised Exception unexpectedly!")
        site.close()

    @timeout_decorator.timeout(50)
    def test_download_save_file(self):
        site = browser.Site()
        site.open()
        try:
            save_manager.download_save_file(site.driver)
        except Exception:
            self.fail("download_save_file() raised Exception unexpectedly!")
        site.close()


class TestClicker(unittest.TestCase):

    @timeout_decorator.timeout(120)
    def test_click_ups(self):
        site = browser.Site()
        site.open()
        try:
            clicker.click_ups(site.driver)
        except Exception:
            self.fail("click_ups() raised Exception unexpectedly!")
        site.close()

    @timeout_decorator.timeout(120)
    def test_print_stats(self):
        site = browser.Site()
        site.open()
        try:
            clicker.print_stats(site.driver)
        except Exception:
            self.fail("print_stats() raised Exception unexpectedly!")
        site.close()

    @timeout_decorator.timeout(120)
    def test_farm(self):
        site = browser.Site()
        site.open()
        try:
            clicker.farm(site.driver, 30)
        except Exception:
            self.fail("farm() raised Exception unexpectedly!")
        site.close()
