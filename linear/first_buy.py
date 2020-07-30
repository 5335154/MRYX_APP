'''首次购物大流程'''
import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:92001',
    'platformVersion':'5.1.1',
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

#点击去支付（提示填写收货地址）
driver.find_element(By.ID,'cn.missfresh.application:id/tv_confirm').click()

#点击收货地址
driver.find_element(By.ID,'cn.missfresh.application:id/tv_address_lable').click()

#新建收货地址
driver.find_element(By.ID,'cn.missfresh.application:id/btn_add_address').click()
driver.find_element(By.ID,'cn.missfresh.application:id/et_edit_address_receiver').clear() #收货人
driver.find_element(By.ID,'cn.missfresh.application:id/et_edit_address_receiver').send_keys('王先生') #收货人
driver.find_element(By.ID,'cn.missfresh.application:id/rg_sex_sir').click() #选择性别
driver.find_element(By.ID,'cn.missfresh.application:id/et_edit_address_tel').clear() #电话号码
driver.find_element(By.ID,'cn.missfresh.application:id/et_edit_address_tel').send_keys('19150855945')
#选择收货地址
driver.find_element(By.ID,'cn.missfresh.application:id/tv_edit_detail_address').click()
driver.find_element(By.ID,'cn.missfresh.application:id/tv_city_name').click()  #选择城市
driver.find_element(By.ID,'cn.missfresh.application:id/et_search_address_input').send_keys('成都市') #输入城市名
driver.find_element(By.ID,'cn.missfresh.application:id/tvCity').click() #选择城市
driver.find_element(By.ID,'cn.missfresh.application:id/et_search_address_input').send_keys('东方广场C座') #输入详细地址关键词
driver.find_element(By.XPATH,'//android.widget.ListView[@resource-id=\"cn.missfresh.application:id/lv_search_content\"]/android.widget.FrameLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').click()  #选择具体地址

driver.find_element(By.ID,'cn.missfresh.application:id/et_edit_doorplate').send_keys("7楼海德学院")#楼号门牌
driver.find_element(By.ID,'cn.missfresh.application:id/rb_company_address_tags').click()  #选择标签
driver.find_element(By.ID,'cn.missfresh.application:id/ssb_default_address_switch').click() #设为默认
driver.find_element(By.ID,'cn.missfresh.application:id/btn_save_address').click() #保存地址

#选择收货地址
driver.find_element(By.ID,'cn.missfresh.application:id/cb_address_default').click()

#点击去支付 (提示存在风险)
driver.find_element(By.ID,'cn.missfresh.application:id/tv_confirm').click()

driver.quit()
