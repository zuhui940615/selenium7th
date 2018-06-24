from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

'''from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element(By.NAME, "username").send_keys("huohuozu")
        driver.find_element(By.NAME, "password").send_keys("123456")
        old_title = driver.title
        driver.find_element(By.CLASS_NAME, "login_btn").click()'''

driver = webdriver.Chrome()
#注意，这里没写隐式等待
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element(By.NAME, "username").send_keys("huohuozu")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CLASS_NAME, "login_btn").click()

#因为中间存在一个登录成功页面，所以不能直接点击该链接
 #解决办法3中方式：time.sleep（），隐式等待，或者显示等待
#WebDriverWait(driver,20,0.5).until(expected_conditions)
WebDriverWait(driver,20,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"进入商城购物")))
#这句显示等待的代码，time.sleep(20)相当于的优化版代码
driver.find_element(By.LINK_TEXT, "进入商城购物").click()
