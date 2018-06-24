from selenium.webdriver.common.by import By


class MemberCenterPage:
    def __init__(self,driver):
        #self.driver = webdriver.Chrome()
        self.driver = driver
        self.url="http://localhost/index.php?m=user&c=index&a=index"

    welcom_link_loc = (By.PARTIAL_LINK_TEXT,"您好")
        #用于返回”你好“链接的所有文本内容
    def get_welcom_link_text(self):
        return self.driver.find_element(*self.welcom_link_loc).text

        #如果当前类中，赋值driver时，没有先用 driver=webdriver.Chrome()
        #那么后面写代码，想用selenium方法时，因为IDE不知道driver的类型，就不会给出提示信息
        #比如，在输入self.driver时，后面不会自动提示find_element()这个方法
