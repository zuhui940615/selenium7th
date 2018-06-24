#这个文件用来实现一个登录功能的自动化操作
#井号表示注释，程序不会运行带井号的语句
#1.打开浏览器
from selenium import webdriver
#从 谷歌公司的一个项目名 导入 网络驱动，用来操作浏览器的
import time

driver = webdriver.Chrome()
#设置智能/隐式等待：一旦找到页面元素，马上执行后面的语句
#如果超过20s，仍然找不到页面元素，那么程序将会报超时错误
driver.implicitly_wait(20)
#2.打开海盗商城网站
driver.get("http://localhost/")
#3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4.输入用户名和密码
driver.find_element_by_id("username").send_keys("huohuozu")
driver.find_element_by_name("password").send_keys("123456")
#5.点击登录按钮
#所有调用方法，都会有提示信息，没有提示信息，就说明没有这个方法
driver.find_element_by_class_name("login_btn").click()
#6.检查登录是否成功，按照现在所学，还不能定位用户名信息，稍后再考虑这个问题
#点击time后，Alt + enter 导包的快捷键，选 import this name,选最短的time
#time.sleep()这个方法提供了一种固定的时间等待
#这里的意义是点击登录按钮后，等5秒后，再检查用户名是否正常显示
#弊端是，因为网络延迟，不知道每次等1秒合适还是等5秒合适
#解决办法：使用智能等待
time.sleep(5)
username_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)
#可以通过if语句判断显示的文本和预期的文本是否一致，来判断测试用例是否正常执行
if username_text =="您好 huohuozu":
    print("测试执行通过")
else:
    print("测试执行失败")
#因为selenium主要做回归测试，所以测试脚本都是pass的，只有开发做了代码变更，我们的测试用例才有可能失败
#一般工作中不用if...else语句做判断，后面再详细讨论这个问题
#7.点击“进入商城购物按钮”
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
#xpath有一个缺点，定位元素的可读性比较差，有没有可读性好一点的方法？
driver.find_element_by_link_text("进入商城购物").click()
#8.在商城主页输入搜索条件“iphone”
driver.find_element_by_name("keyword").send_keys("iphone")
#9.点击“搜索按钮”
driver.find_element_by_class_name("btn1").click()
#10.在搜索结果页面，点击第一个商品的图片
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img").click()
#窗口切换
driver.close()#关闭selenium正在工作的窗口
driver.switch_to.window(driver.window_handles[-1])
#11.点击“加入购物车”
driver.find_element_by_id("joinCarButton").click()