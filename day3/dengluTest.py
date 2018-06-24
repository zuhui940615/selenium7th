#selenium执行javascript中的两个关键字：return返回值和argument参数
from selenium import webdriver

from selenium.webdriver.support.select import Select

import time
from webdriver import ActionChains
from webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.implicitly_wait(20)
driver.get("http://localhost/")
#点击“登录链接”
#用js的方法找登录链接的代码：
#document.getElementByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接的代码：
#driver.find_element_by_link_text("登录")
#某些元素，用s的方法找比js更容易
#虽然s不支持removeAttribute的方法
#但是s找到的登录链接和j找到的是同一个元素
#w我们可不可以用selenium找到元素之后，转换成javascript的元素？
#这样以后写java就容易很多，不需要childNodes这些方法了
#比如，driverdriver.find_element_by_link_text("登录").removeAtribute()
#driver.execute_script("document.get)
login_link=driver.find_element_by_link_text("登录")
#把selenium找到的这个元素，传入到java的方法里，代替原来jav的定位。原来的iavas看成是一个无参无返的方法，现在直接懂外面传入一个页面元素，就变成了一个有参无返的方法
#argument是参数的复数形式，[0]表示第一个参数，指的就是js后面login—link
#所以下面这句代码，相当于把driver.find_elements_by_link_text("登录")带入到js语句中
#变成了driver.find_elements_by_link_text("登录").removeAttribute('target')
#a是参数数组，指的是js字符串后面的所有参数
#一般情况下我们只会用到[0]，既js后面的第一个参数
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#执行成功的自己写登录
driver.find_element_by_id("username").send_keys("huohuozu")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
#返回商城首页
driver.find_element_by_link_text("进入商城购物").click()
#搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#点击商品（用这种方法，再实现一次不打开新窗口）
#使用js删除a标签的targrt属性
#因为img没有target属性，所以我们复制css的时候要找他的父节点a标签
#复制出来的css往往比较长，我们可以适当的缩写长度
#我们定定位元素的目标节点是最后一个节点，不能删
#大于号>的前面是父节点，后面是子节点
#每个节点的第一个单词是表签名，比如：a，div，body
#小数点后面表示class属性
#：nth-child（2），nth表示第几个，4th，5th，nth表示第n个，child表示子节点
#所以，：nth-child（2）表示当前标签是它的父节点的第二个子节点
product_link_css="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a"
#通过css-selector定位元素
iphone = driver.find_element_by_css_selector(product_link_css)
#删除元素的target属性
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
#在商品详情界面，点击加入购物车
driver.find_element_by_id("joinCarButton").click()
#driver.find_elements_by_class_name("shopCar_T_span3").click()
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击“结算”按钮
#在每个class前面都加一个小数点，并且去掉中间的空格，我们就可以同时用两个属性定位一个元素
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
#driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[3]/a").click()
#点击“添加新地址”
driver.find_element_by_css_selector(".add-address").click()
#输入收货人等信息（选择地区下午讲）
driver.find_element_by_name("address[address_name]").send_keys("huohuozu")
driver.find_element_by_name("address[mobile]").send_keys("13521141985")
dropdown1 = driver.find_element_by_id("add-new-area-select")
#下拉框是一种特殊的网页元素，对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素，专门创建了一个类Select
#dropdown1的类型是一个普通的网页元素，下面这句话的意思，是把一个普通的网页元素，转换成一个下拉框的特殊网页元素
print(type(dropdown1))#dropdown1是Web_element类型
#WebElement这个类中，只有click和send_keys这样的方法，没有选择下拉框选项的方法
select1 = Select(dropdown1)#select1是Select类型
#转换成Select类型之后，网页元素还是那个网页元素，但是Select类中有选择选项的方法
select1.select_by_value("320000")#这时，我们就可以通过选项的值来定位
time.sleep(2)
select1.select_by_visible_text("辽宁省")#也可以通过选项的文本信息来定位
#选择沈阳市
#因为是动态id，所以不能通过id来定位
#因为class重复，所以也不能直接用class定位
#但是可以用find_elements的方法，先找到页面所有class=add-new-area-select的元素
# 然后再通过下标的方式选择第n个页面元素
#这种方法类似于以前学的javascript方法
dropdown2 = driver.find_elements_by_class_name("add-new-area-select")[1]
select2 = Select(dropdown2)
select2.select_by_value("210100")
#铁西区
#dropdown3 = driver.find_elements_by_class_name("add-new-area-select")[2]等同于下面这句
dropdown3 = driver.find_elements_by_tag_name("select")[2]
#tag_name()这个方法大多数情况都能找到一堆元素
# 所以find_element_tag_name()这个方法很少用
# 但是find_elements_tag_name()很常用
select3=Select(dropdown3)
select3.select_by_visible_text("铁西区")

#填写“详细地址”
driver.find_element_by_name("address[address]").send_keys("辽宁大学东城区")
driver.find_element_by_name("address[zipcode]").send_keys("810058")
# 点击“确定”，保存收货人信息
driver.find_element_by_class_name("aui_state_highlight").click()
#点击“取消”按钮
# driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()