from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://cn.bing.com/')

# 获取文本框
input_tag = driver.find_element_by_id('sb_form_q')

# 获取按钮
button = driver.find_element_by_id('sb_form_go')

# 创建行为链（模拟人类行为）
actions = ActionChains(driver=driver)

# 移动到文本框
actions.move_to_element(input_tag)
# 在文本框上输入关键字
actions.send_keys_to_element(input_tag, 'python')

# 移动到搜索按钮
actions.move_to_element(button)

# 点击搜索
actions.click(button)

# 提交行为链
actions.perform()