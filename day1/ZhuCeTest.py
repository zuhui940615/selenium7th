#在这个pythowebn文件中，实现注册功能的自动化
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("huohuo")
driver.find_element_by_name("password").send_keys("huohuo")
driver.find_element_by_name("userpassword2").send_keys("huohuo")
driver.find_element_by_name("mobile_phone").send_keys("13601606815")
driver.find_element_by_name("email").send_keys("414300691@qq.com")
driver.find_element_by_class_name("reg_btn").click()