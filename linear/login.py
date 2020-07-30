'''登录'''
import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:62001',
    'platformVersion':'5.1.1',
    'appPackage':'cn.missfresh.application',
    'appActivity':'cn.missfresh.module.base.main.view.SplashActivity',
    'newCommandTimeout':600
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
driver.implicitly_wait(30)
#用户隐私保护提示，点击同意
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_double_btn_ok"]').click()
#点击我的
driver.find_element(By.ID,'cn.missfresh.application:id/mineTab').click()
#点击登录/注册
driver.find_element(By.ID,'cn.missfresh.application:id/tv_nickname').click()
#勾选同意协议
driver.find_element(By.ID,'cn.missfresh.application:id/iv_protocol').click()
#微信登录
driver.find_element(By.ID,'cn.missfresh.application:id/tv_wx_login').click()
time.sleep(2)
driver.quit()