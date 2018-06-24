#1.导包
import unittest
from selenium import webdriver

#2.继承unittest.TestCase
import time

from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class ReisterTest(unittest.TestCase):
    #3.重写setup和teardown方法
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

            #4.编写一个测试用例方法（以test开头的方法）
    def test_register(self):
        for row in CsvFileManager4().read("test_data.csv"):
            driver = self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            #driver.find_element(By.NAME,"username")==driver.find_element_by_name("username")
            #这两种方法没有任何区别，但是后面的这种方法扩展性更好，便于框架封装
            #driver.find_element_by_name("username")
            driver.find_element(By.NAME, "username").send_keys(row[0])
            driver.find_element(By.NAME, "password").send_keys(row[1])
            driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
            driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME, "email").send_keys(row[4])
            #driver.find_element(By.CLASS_NAME, "reg_btn").click()
            #在for循环中执行测试用例，虽然解决了批量执行的问题，但是，如果第一行测试用例执行失败，后续的测试用例还会不会执行
#考虑异常情况，输入完邮箱后，按tab键，检查提示信息是否都是“通过信息验证！”
#怎么验证？如果页面上提示的信息是“通过信息验证！”，那么，测试通过，否则测试失败
            #body > div.w1180 > div > div.reg_main > div.reg_left.fl >
            check_tip = driver.find_element(By.CSS_SELECTOR,"form.registerform.sign > ul > li:nth-child(1) > div > span").text
            print(check_tip)
            #其中check_tip是执行用例时，从网页上抓取的实际结果
            #“通过信息验证！”是来自于手工测试用例，是测试用例执行的期望结果

            #if check_tip=="通过信息验证！":
               # print("测试通过")
           # else:
               # print("测试失败")
                #这样通过if...else语句，就可以自动判断测试用例的执行情况
                #断言的写法
            self.assertEqual("通过信息验证！",check_tip)
#虽然第一条测试数据执行失败了，但是后面的测试是不依赖前面的，不应该因为第一条失败就导致其他数据不执行测试
#所以我们不应该用for循环的方式执行不同烦人测试数据，
#因为在方法中写了for循环虽然执行了多次，但是unittest仍然认为他是一条测试用例，一旦断言失败，就会种植这条测试用例
#所以我们应该曹采用ddt框架实现数据驱动


if __name__ == '__main__':
    unittest.main()