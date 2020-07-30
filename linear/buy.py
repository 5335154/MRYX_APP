'''购物大流程'''
import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:92001',
    'plarformVersion':'5.1.1',
    'appPackage':'cn.missfresh.application',
    'appActivity':'cn.missfresh.module.base.main.view.SplashActivity',
    'newCommandTimeout':600,
    'noReset':True,
    'unicodeKeyboard':True,
    'resetKeyboard':True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
driver.implicitly_wait(30)

#点击购物车
driver.find_element(By.ID,'cn.missfresh.application:id/cartTab').click()

#去逛逛
driver.find_element(By.ID,'cn.missfresh.application:id/tv_go').click()

#选择地址
driver.find_element(By.ID,'cn.missfresh.application:id/iv_address_icon').click()
driver.find_element(By.ID,'cn.missfresh.application:id/tv_select_support_city').click()
driver.find_element(By.ID,'cn.missfresh.application:id/et_search_address_input').send_keys("成都市")
driver.find_element(By.ID,'cn.missfresh.application:id/tvCity').click()
driver.find_element(By.ID,'cn.missfresh.application:id/iv_title_bar_left_icon').click()
time.sleep(2)

#导航栏向左滑，向右滑
size = driver.get_window_size()
print(size)
driver.swipe(size['width']*0.8,100,size['width']*0.2,100)  #向左滑
time.sleep(1)
driver.swipe(size['width']*0.2,100,size['width']*0.8,100)  #向右滑

#点击时令水果
locator = driver.find_element(By.ID,'cn.missfresh.application:id/tab_layout')
locator.find_element(By.XPATH,'//android.widget.TextView[2]').click()

#点击第二个商品的“+”
locator = driver.find_element(By.ID,'cn.missfresh.application:id/recycler_view')
locator.find_element(By.XPATH,'//android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.ImageView').click()

#同时点击1、2、3的“+”
driver.tap([(241,370),(508,370),(241,647)],500)

#查看第四个商品的详情
locator = driver.find_element(By.ID,'cn.missfresh.application:id/recycler_view')
locator.find_element(By.XPATH,'//android.widget.RelativeLayout[4]/android.widget.ImageView[1]').click()

#加入购物车
locator = driver.find_element(By.ID,'cn.missfresh.application:id/rc_ll_btns') #找到父级
locator.find_element(By.XPATH,'//android.widget.TextView[1]').click()

#立即购买
locator = driver.find_element(By.ID,'cn.missfresh.application:id/rc_ll_btns') #找到父级
locator.find_element(By.XPATH,'//android.widget.TextView[2]').click()

#勾选同意协议
driver.find_element(By.ID,'cn.missfresh.application:id/iv_protocol').click()

#微信登录
driver.find_element(By.ID,'cn.missfresh.application:id/tv_wx_login').click()

#立即购买
locator = driver.find_element(By.ID,'cn.missfresh.application:id/rc_ll_btns') #找到父级
locator.find_element(By.XPATH,'//android.widget.TextView[2]').click()
time.sleep(2)
#选择支付宝
driver.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/confirm_recycler_view"]/android.widget.RelativeLayout[6]/android.widget.ImageView[2]').click()

#点击去支付 (提示存在风险)
driver.find_element(By.ID,'cn.missfresh.application:id/tv_confirm').click()

driver.quit()
