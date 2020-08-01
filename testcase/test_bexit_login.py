import unittest

from driver.android_driver import app_driver
from page.my_page import MyPage

class Exit_LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = app_driver()
    def tearDown(self):
        self.driver.quit()

    def test_exit_login(self):
        lg = MyPage(self.driver)
        result = lg.exit_login()

        self.assertEqual("登录/注册", result)


if __name__ == '__main__':
    unittest.main()
