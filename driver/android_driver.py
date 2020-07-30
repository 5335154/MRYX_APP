from appium import webdriver

def app_driver():
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '5.1.1',
        'appPackage': 'cn.missfresh.application',
        'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
        'newCommandTimeout': 600,
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(30)
    return driver