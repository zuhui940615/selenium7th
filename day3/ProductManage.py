#1.登录海盗商城的后台
from selenium import webdriver

import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
#2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/a[2]").click()
#3.点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
#4.输入商品名称
#操作子框架中的元素，首先要进行frame切换
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphoneX")
#5.选择商品分类（双击或者点击“选择当前分类”）
driver.find_element_by_id("jiafen").click()
driver.find_element_by_id("jiafen").click()
#6.再下拉框中选择商品品牌
dropdown = driver.find_elements_by_class_name("select")[1]
select = Select(dropdown)
select.select_by_value("1")
#7.点击提交按钮
driver.find_element_by_class_name("button_search").click()

#根据以上7步，编写代码，找出第一个不能实现的地方