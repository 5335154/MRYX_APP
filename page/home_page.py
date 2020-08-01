import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.my_page import MyPage


class HomePage():
    '''首页'''
    def __init__(self,driver):
        self.driver = driver
        #元素定位符
        self.loc_location = (By.ID, 'cn.missfresh.application:id/iv_address_icon') #左上角定位
        self.loc_choice_city = (By.ID, 'cn.missfresh.application:id/tv_select_support_city') #选择城市
        self.loc_input_city = (By.ID, 'cn.missfresh.application:id/et_search_address_input') #输入城市
        self.loc_input_choice_city = (By.ID, 'cn.missfresh.application:id/tvCity')  #输入后选择城市
        self.loc_back = (By.ID, 'cn.missfresh.application:id/iv_title_bar_left_icon') #返回
        self.loc_input_adress = (By.ID, 'cn.missfresh.application:id/et_search_input')  #输入收货地址
        self.loc_click_adress = (By.XPATH,'//*[@text="四川省成都市锦江区东大街芷泉段229"]') #点击地址
        self.loc_assert = (By.XPATH,'//*[@text="送至:东方广场C座"]') #断言
        self.loc_click_navigation = (By.XPATH,'//*[@text="时令水果"]') #时令水果
        self.loc_click_goods_father = (By.ID, 'cn.missfresh.application:id/recycler_view') #商品栏父级
        self.loc_click_goods = (By.XPATH,'//android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.ImageView') #点击第二个商品+
        self.loc_view_goods = (By.XPATH, '//android.widget.RelativeLayout[4]/android.widget.ImageView[1]')
        self.loc_join_shopping_cart = (By.XPATH,'//*[@text="加入购物车"]')  # 加入购物车
        self.loc_buying = (By.XPATH,'//*[@text="立即购买"]') #立即购买
        self.loc_settlement = (By.ID,'cn.missfresh.application:id/tv_checkout') #去结算
        self.loc_shopping_address = (By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_address_lable"]') #点击选择收货地址
        self.loc_choice_adress = (By.XPATH,'//android.widget.ListView[@resource-id="cn.missfresh.application:id/lv_address"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]') #选择收货地址
        self.loc_pay = (By.ID,'cn.missfresh.application:id/tv_confirm') #去支付
        self.loc_assert_two = (By.XPATH,'//*[@text="设备存在风险，请更换设备下单"]') #断言

    def ele_location(self): #左上角定位
        self.driver.find_element(*self.loc_location).click()

    def ele_choice_city(self): #选择城市
        self.driver.find_element(*self.loc_choice_city).click()

    def ele_input_city(self,city): #输入城市，选择城市
        self.driver.find_element(*self.loc_input_city).send_keys(city)
        self.driver.find_element(*self.loc_input_choice_city).click()

    def ele_back(self):  #返回
        self.driver.find_element(*self.loc_back).click()

    def ele_input_adress(self,adress): #输入收货地址
        self.driver.find_element(*self.loc_input_adress).send_keys(adress)  #输入收货地址 东方广场C座

    def ele_click_adress(self):  #选择地址
        self.driver.find_element(*self.loc_click_adress).click()

    # def ele_wait_toast(self):  #等待 toast弹窗
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(lambda driver: driver.find_element(*self.loc_assert))

    def ele_click_navigation(self):  #点击时令水果
        self.driver.find_element(*self.loc_click_navigation).click()
        time.sleep(1)
        self.driver.save_screenshot('../screenshot/时令水果.png')

    def ele_click_goods(self):  # 点击第二个商品的“+”
        locator = self.driver.find_element(*self.loc_click_goods_father)
        locator.find_element(*self.loc_click_goods).click()

    def ele_tap_goods(self):  # 同时点击1、2、3的“+”
        self.driver.tap([(482, 743), (1015, 743), (482, 1288)], 500)
        self.driver.save_screenshot('../screenshot/添加购物车.png')

    def ele_view_goods(self):  # 查看第四个商品的详情
        locator = self.driver.find_element(*self.loc_click_goods_father)
        locator.find_element(*self.loc_view_goods).click()

    def ele_join_shopping_cart(self):  # 加入购物车
        self.driver.find_element(*self.loc_join_shopping_cart).click()
        time.sleep(1)
        self.driver.save_screenshot('../screenshot/加入购物车(显示数量).png')

    def ele_buying(self):  # 立即购买
        self.driver.find_element(*self.loc_buying).click()

    def ele_settlement(self): #去结算
        self.driver.find_element(*self.loc_settlement).click()

    def ele_shopping_adress(self):  #点击选择收货地址
        self.driver.find_element(*self.loc_shopping_address).click()

    def ele_choice_adress(self):  #选择收货地址
        self.driver.find_element(*self.loc_choice_adress).click()

    def ele_pay(self):  #去支付
        self.driver.find_element(*self.loc_pay).click()
        self.driver.save_screenshot('../screenshot/收货地址.png')

    def ele_assert_two(self): #断言
        wait = WebDriverWait(self.driver,10)
        wait.until(lambda driver:driver.find_element(*self.loc_assert_two))

    def flow_buy(self):
        '''购物流程'''
        self.ele_click_navigation()   # 点击时令水果
        self.ele_click_goods()        # 点击第二个商品的“+”
        self.ele_tap_goods()          # 同时点击1、2、3的“+”
        self.ele_view_goods()         # 查看第四个商品的详情
        self.ele_join_shopping_cart() # 加入购物车
        self.ele_buying()             # 立即购买
        MyPage(self.driver).wechat_login() # 微信登录
        self.ele_buying()             # 立即购买
        self.ele_shopping_adress()    # 点击选择收货地址
        self.ele_choice_adress()      # 选择收货地址
        self.ele_pay()                # 去支付
        self.ele_assert_two()         #断言
        result = self.driver.find_element(*self.loc_assert_two).text  #断言
        return result

    def adress(self,city,adress):
        '''选择收货地址'''
        self.ele_location()
        self.ele_choice_city()
        self.ele_input_city(city)
        self.ele_input_adress(adress)
        self.ele_click_adress()
