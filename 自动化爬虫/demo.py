from selenium import webdriver

chrome = webdriver.Chrome()

# 请求的url
chrome.get('https://www.baidu.com/')

# 截图保存
chrome.save_screenshot('baidu.png')
# 获取源代码
html = chrome.page_source
print(html)

# 关闭浏览器窗口
chrome.quit()
