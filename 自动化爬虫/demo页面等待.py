from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait   # 显示de等待
from selenium.webdriver.common.by import By   # 通过什么获取
from selenium.webdriver.support import expected_conditions as ec   # 期望条件

driver = webdriver.Chrome()

# driver.get('https://www.baidu.com/')
#
# # 隐式等待，等待5秒钟
# driver.implicitly_wait(5)
# driver.find_element_by_id('abc')

# 显示等待
driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')

# 等待文本框中输入内容    等待100秒   出发地长沙  通过ID获取
WebDriverWait(driver, 100).until(
    ec.text_to_be_present_in_element_value((By.ID, 'fromStationText'), '长沙')
)

# 目的地   成都     通过ID获取
WebDriverWait(driver, 100).until(
    ec.text_to_be_present_in_element_value((By.ID, 'toStationText'), '成都')
)
btn = driver.find_element_by_id('query_ticket')
btn.click()
