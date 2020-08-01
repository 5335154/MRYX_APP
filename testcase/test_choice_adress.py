import unittest

from driver.android_driver import app_driver
from page.home_page import HomePage


class Choice_AdressTestCase(unittest.TestCase):
    '''选择收货地址'''
    def setUp(self):
        self.driver = app_driver()

    def tearDown(self):
        self.driver.quit()

    def test_choice_adress(self):
        home = HomePage(self.driver)
        home.adress("成都市","东方广场C座")

if __name__ == '__main__':
    unittest.main()
