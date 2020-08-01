import time

from selenium.webdriver.common.by import By

from base_page.base import left_swipe, right_swipe
from page.shopping_cart_page import Shopping_CartPage


class First_BuyPage():
    def __init__(self,driver):
        self.driver = driver

    def ele_click_shopping_cart(self):  # 点击购物车
        sc = Shopping_CartPage(self.driver)
        sc.shopping_cart()

    def ele_home_page(self):  # 去逛逛
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_go').click()

    def ele_select_address(self):  # 选择地址
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/iv_address_icon').click()
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_select_support_city').click()
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_search_address_input').send_keys("成都市")
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tvCity').click()
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/iv_title_bar_left_icon').click()
        time.sleep(2)

    def ele_left_right_swipe(self):    # 导航栏向左滑，向右滑
        left_swipe(self)
        time.sleep(1)
        right_swipe(self)

    def ele_click_fruits(self):    # 点击时令水果
        locator = self.driver.find_element(By.ID, 'cn.missfresh.application:id/tab_layout')
        locator.find_element(By.XPATH, '//android.widget.TextView[2]').click()
        self.driver.save_screenshot('../screenshot/时令水果.png')

    def ele_click_goods(self):    # 点击第二个商品的“+”
        locator = self.driver.find_element(By.ID, 'cn.missfresh.application:id/recycler_view')
        locator.find_element(By.XPATH,'//android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.ImageView').click()

    def ele_tap_goods(self):    # 同时点击1、2、3的“+”
        self.driver.tap([(241, 370), (508, 370), (241, 647)], 500)
        self.driver.save_screenshot('../screenshot/添加购物车.png')

    def ele_view_goods(self):    # 查看第四个商品的详情
        locator = self.driver.find_element(By.ID, 'cn.missfresh.application:id/recycler_view')
        locator.find_element(By.XPATH, '//android.widget.RelativeLayout[4]/android.widget.ImageView[1]').click()

    def ele_join_shopping_cart(self):    # 加入购物车
        locator = self.driver.find_element(By.ID, 'cn.missfresh.application:id/rc_ll_btns')  # 找到父级
        locator.find_element(By.XPATH, '//android.widget.TextView[1]').click()
        self.driver.save_screenshot('../screenshot/加入购物车(数量).png')

    def ele_buy(self):    # 立即购买
        locator = self.driver.find_element(By.ID, 'cn.missfresh.application:id/rc_ll_btns')  # 找到父级
        locator.find_element(By.XPATH, '//android.widget.TextView[2]').click()

    def ele_yes(self):    # 勾选同意协议
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/iv_protocol').click()

    def ele_wechat_login(self):    # 微信登录
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_wx_login').click()

    def ele_buying(self):    # 立即购买
        locator = self.driver.find_element(By.ID, 'cn.missfresh.application:id/rc_ll_btns')  # 找到父级
        locator.find_element(By.XPATH, '//android.widget.TextView[2]').click()
        time.sleep(2)

    def ele_alipay(self):  # 选择支付宝
        self.driver.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/confirm_recycler_view"]/android.widget.RelativeLayout[6]/android.widget.ImageView[2]').click()

    def ele_go_to_pay(self):    # 点击去支付（提示填写收货地址）
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_confirm').click()

    def ele_click_adress(self):    # 点击收货地址
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_address_lable').click()

    def ele_create_adress(self):    # 新建收货地址
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/btn_add_address').click()
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_edit_address_receiver').clear()  # 收货人
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_edit_address_receiver').send_keys('王先生')  # 收货人
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/rg_sex_sir').click()  # 选择性别
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_edit_address_tel').clear()  # 电话号码
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_edit_address_tel').send_keys('19150855945')

    def ele_choice_adress(self):    # 选择收货地址
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_edit_detail_address').click()
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_city_name').click()  # 选择城市
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_search_address_input').send_keys('成都市')  # 输入城市名
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tvCity').click()  # 选择城市
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_search_address_input').send_keys('东方广场C座')  # 输入详细地址关键词
        self.driver.find_element(By.XPATH,'//android.widget.ListView[@resource-id="cn.missfresh.application:id/lv_search_content"]/android.widget.FrameLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').click()  # 选择具体地址
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/et_edit_doorplate').send_keys("7楼海德学院")  # 楼号门牌
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/rb_company_address_tags').click()  # 选择标签
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/ssb_default_address_switch').click()  # 设为默认
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/btn_save_address').click()  # 保存地址

    def ele_adress(self):    # 选择收货地址
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/cb_address_default').click()

    def ele_click_go_to_pay(self):    # 点击去支付 (提示存在风险)
        self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_confirm').click()

    def jinqu(self):
        self.ele_click_shopping_cart()
        self.ele_home_page()
        self.ele_select_address()
        self.ele_left_right_swipe()