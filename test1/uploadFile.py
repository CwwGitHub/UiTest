import time
from selenium import webdriver

# 用谷歌浏览器，打开百度识图页面
driver = webdriver.Chrome()
driver.get("https://graph.baidu.com/pcpage/index?tpl_from=pc")
driver.maximize_window()

time.sleep(2)
driver.find_element("class name","graph-d20-search-wrapper-camera").click() # 点击照相机图标
driver.find_element("name","file").send_keys("C:\\Users\\cww\\Pictures\\500X400.jpg") #定位到input有带type="file"的元素，然后发送图片的路径
