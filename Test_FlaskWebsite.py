import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#pytest+selenium

class TestFlaskWebsite:
    #用正确的用户名和密码，测试登录是否成功
    @pytest.mark.parametrize('homeurl,username,password',[("http://localhost:5001","username1","password1")])
    def test_site_login_success(self,homeurl,username,password):
        driver = webdriver.Chrome()
        driver.get(homeurl)
        driver.find_element(By.LINK_TEXT,"登录").click()
        driver.find_element(By.NAME,"username").send_keys(username)
        driver.find_element(By.NAME,"password").send_keys(password)
        driver.find_element("XPATH","//button[text()=登录").click()

        #验证界面上是否显示了用户名
        assert driver.find_element(By.ID,"user").text==username
        #验证界面上是否显示“登出”链接
        assert len(driver.find_element(By.LINK_TEXT,"登出"))==1
        driver.quit()

    #用错误的用户名和密码，测试登录是否失败
    @pytest.mark.parametrize("homeUrl,errorUsername,errorPassword",[("http://localhost:5001","errorUser1","errorPwd1")])
    def test_site_losin_fail(self,homeUrl,errorUsername,errorPassword):
        driver = webdriver.Chrome()
        driver.get(homeUrl)
        driver.find_element(By.LINK_TEXT,"登录").click()
        driver.find_element(By.NAME,"username").send_keys(errorUsername)
        driver.find_element(By.NAME,"password").send_keys(errorPassword)
        driver.find_element(By.XPATH,"//button[text()='登录']").click()

        #验证界面上是否显示“用户名或密码错误！“
        assert driver.find_element(By.TAG_NAME,"h4").text=="用户名或密码错误！"

        driver.quit()