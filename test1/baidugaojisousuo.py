#【需求】在百度 - 设置 - 高级搜索界面，时间下拉框选择最近一月
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# 用谷歌浏览器，打开百度一下页面
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

# 定位【设置】元素,并把鼠标悬停在【设置】上
move = driver.find_element("id","s-usersetting-top")
ActionChains(driver).move_to_element(move).perform()
time.sleep(4)

#定位到“搜索设置”，然后点击
driver.find_element("link text","高级搜索").click()

#点击下拉框，展开可选项，让之后可以点击某个可选项
time.sleep(2)
driver.find_element("class name","adv-gpc-select").click()
time.sleep(2)
driver.find_element("xpath","//div[@class='c-select adv-gpc-select c-select-visible visible']//p[5]").click()

time.sleep(5)
driver.close()