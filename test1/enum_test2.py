
from enum import Enum

import time
from selenium import webdriver
import pytest

# 用Chrome浏览器，打开url
driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc")
driver.maximize_window()
time.sleep(2)
# 默认选择出发地（北京）、目的地（福州）、出发日（今天）、车次类型后，点击查询
fromStation = driver.find_element("id","fromStationText")
fromStation.clear()
fromStation.send_keys("北京")
toStation = driver.find_element("id","toStationText")
toStation.clear()
toStation.send_keys("福州")
elem = driver.find_element("xpath","//a[@id='query_ticket']")
elem.click()
print("点击查询按钮")


# 车型枚举
class TrainTypeEnum(Enum):
    GaoTie = 'G' # GC-高铁/城际
    DongChe = 'D' # D-动车
    ZhiDa = 'Z' # Z-直达
    TeKuai = 'T' # T-特快
    KuaiSu = 'K' # K-快速
    QiTa ='QT' # QT-其他

# 选择车型
def select_train_tpye(self,train_type_enum):

    print("train_type_enum.name:",train_type_enum.name)
    print("select train by '{}'".format(train_type_enum.name))
    elem = self.browser.find_element_by_css_selector("#_ul_station_train_code > li > input.check[value='{}']".format(train_type_enum.value))
    if not elem.is_selected():
        elem.click()
    return self


# test_开头的方法代表使用unittest模块
# 验证车型筛选结果
def test_train_type_filter():
    # 调用选择车型方法
    filter_train_type = TrainTypeEnum.TeKuai
    print("测试类：",filter_train_type.value)

    select = driver.select_train_type(filter_train_type)
    # 默认选择出发地（北京）、目的地（福州）、出发日（今天）、车次类型后，点击查询
    #driver.find_element(id('query_ticket')).click()


    # 存放车型筛选结果
    filtered_trains=[]

    for train in filtered_trains:
        assert train.startswith(filter_train_type.value)

time.sleep(3)
#driver.quit()














