
import time
import unittest


from selenium import webdriver




class Bolg(unittest.TestCase):
    u'''登录博客园'''
    # 用Chrome浏览器打开博客园登录页面
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)


    # 登录：输入账号密码，点登录按钮
    def login(self,username,password):
        u'''这里写了一个登录的方法，把账号和密码参数化'''
        self.driver.find_element("id","mat-input-0").send_keys(username)
        self.driver.find_element("id","mat-input-1").send_keys(password)
        self.driver.find_element("xpath","//button[@class='mat-focus-indicator action-button ng-tns-c139-2 mat-flat-button mat-button-base mat-primary']//span[@class='mat-button-wrapper']").click()
        time.sleep(3)


    # 判断是否登录成功，登录成功，则获取账号名，并返回true，登录失败，则返回false
    def is_login_sucess(self):
        u'''判断是否获取登录账户名称(右上角的账户名)'''
        try:
            text = self.driver.find_element("xpath","//body/div/div/div/div[1]/a[2]").text
            print("登录成功，其用户名为(预期为乔伊cww)："+text)
            return True
        except:
            return False


    # 测试用例——登录成功
    def test_01(self):
        u'''登录案例参考：账号，密码自己设置'''
        # 调用登录方法
        self.login(u"wwchen",u"cww12345")
        # 调用判断是否登录成功的方法
        result = self.is_login_sucess()
        # 判断结果
        self.assertTrue(result)


    # 测试用例——登录失败,用户名错误
    def test_02(self):
        u'''登录案例参考：账号，密码自己设置'''
        # 调用登录方法
        self.login(u"ww", u"cww12345")
        # 调用判断是否登录成功的方法
        result = self.is_login_sucess()
        # 判断结果
        self.assertTrue(result)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

