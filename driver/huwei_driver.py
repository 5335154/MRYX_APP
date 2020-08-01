from appium import webdriver




def hw_driver():

    desired_capbilities ={'platformName':'Android',
                          'deviceName': 'yesheng',
                          'platformVersion': '5.1.1',
                          'appPackage': 'cn.missfresh.application',
                          'appActivity': 'cn.missfresh.module.base.main.view.MainActivity',
                          'unicodeKeyboard': True,
                          'resetKeyboard': True}
    driver = webdriver.Remote('http://192.168.1.83:4723/wd/hub', desired_capbilities)
    driver.implicitly_wait(10)
    return driver

