import time
from selenium.webdriver.common.by import By


class Shopping_CartPage():
    '''购物车页面'''
    def __init__(self, driver):
        self.driver = driver
        # 定位
        self.loc_shopping_cart = (By.ID, 'cn.missfresh.application:id/cartTab') #点击购物车
        self.loc_add_goods_one = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.RelativeLayout[1]/android.widget.ImageView[3]') #添加商品1
        self.loc_add_goods_two = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.RelativeLayout[2]/android.widget.ImageView[3]') #添加商品2
        self.loc_assert_add = (By.ID,'cn.missfresh.application:id/tv_checkout')  #添加成功断言
        self.loc_add_number = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[5]') #增加数量
        self.loc_reduce_number = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/rcv_product\"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[4]')  #减少数量
        self.loc_view_details = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/rcv_product"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]') #查看详情
        self.loc_back = (By.ID, 'cn.missfresh.application:id/img_back') #返回
        self.loc_deselect = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/rcv_product"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]') #取消一个选中
        self.loc_delete = (By.ID, 'cn.missfresh.application:id/tv_delete') # 删除
        self.loc_delete_no = (By.ID, 'cn.missfresh.application:id/tv_search') #取消删除
        self.loc_select_all = (By.XPATH,'//android.widget.LinearLayout[@resource-id="cn.missfresh.application:id/sticky"]/android.widget.ImageView[1]') #全选
        self.loc_delete_yes = (By.ID, 'cn.missfresh.application:id/tv_ensure') #确定删除

    def ele_shopping_cart(self):  # 点击购物车
        self.driver.find_element(*self.loc_shopping_cart).click()

    def ele_add_goods(self):  # 添加两件商品
        self.driver.find_element(*self.loc_add_goods_one).click()
        time.sleep(2)
        self.driver.find_element(*self.loc_add_goods_two).click()

    def ele_assert(self):  #断言
        result = self.driver.find_element(*self.loc_assert_add).get_attribute('clickable')
        return result

    def ele_add_number(self,add_num):   # 增加数量5个
        for i in range(add_num):
            self.driver.find_element(*self.loc_add_number).click()

    def ele_reduce(self,reduce_num):   # 减少数量3个
        for m in range(reduce_num):
            self.driver.find_element(*self.loc_reduce_number).click()

    def ele_view_details(self):  # 查看详情
        self.driver.find_element(*self.loc_view_details).click()

    def ele_back(self):  # 返回
        self.driver.find_element(*self.loc_back).click()

    def ele_deselect(self):  # 取消一个选中
        self.driver.find_element(*self.loc_deselect).click()

    def ele_delete_no(self):# 删除-取消
        self.driver.find_element(*self.loc_delete).click()
        self.driver.find_element(*self.loc_delete_no).click() #取消

    def ele_select_all(self): # 全选
        self.driver.find_element(*self.loc_select_all).click()

    def ele_delete_yes(self):# 删除-确定
        self.driver.find_element(*self.loc_delete).click()
        self.driver.find_element(*self.loc_delete_yes).click() #确定
        self.driver.save_screenshot('../screenshot/删除.png')

    def add_goods(self):
        '''猜你喜欢，加入购物车'''
        self.ele_shopping_cart()
        self.ele_add_goods()
        result = self.ele_assert()
        return result


    def shopping_cart(self,add_num,reduce_num):
        '''购物车改-查-删'''
        self.ele_shopping_cart()
        self.ele_add_goods()
        result = self.ele_assert()
        self.ele_add_number(add_num)  #增加数量
        self.ele_reduce(reduce_num)   #减少数量
        self.ele_view_details()
        self.ele_back()
        self.ele_deselect()
        self.ele_delete_no()
        self.ele_select_all()
        self.ele_delete_yes()
        return result

