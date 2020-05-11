import unittest
import browser
import save_manager
import timeout_decorator


class TestBrowser(unittest.TestCase):

    @timeout_decorator.timeout(50)
    def test_open_and_close(self):
        site = browser.Site()
        try:
            site.open()
        except Exception:
            self.fail("site.open() raised ExceptionType unexpectedly!")

        try:
            site.close()
        except Exception:
            self.fail("site.close() raised ExceptionType unexpectedly!")


class TestSaveManager(unittest.TestCase):

    @timeout_decorator.timeout(50)
    def test_open_options(self):
        site = browser.Site()
        site.open()
        try:
            save_manager._open_options(site.driver)
        except Exception:
            self.fail("_open_options() failed!")
