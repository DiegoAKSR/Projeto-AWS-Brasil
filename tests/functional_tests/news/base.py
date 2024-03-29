import time

from django.test import LiveServerTestCase

from utils.browser import make_chome_browser


class NewsBaseTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = make_chome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)
