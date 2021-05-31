import urllib.request
from http import cookiejar

filename = 'cookie.txt'


# 获取Cookie
def get_cookie():
    """
    实例化一个MozillaCookieJar，用于保存cookie
    :return:
    """
    # 保存cookie
    cookie = cookiejar.MozillaCookieJar(filename)

    # 创建handler对象, cookie的处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)

    # 创建opener对象
    opener = urllib.request.build_opener(handler)

    url = 'https://tieba.baidu.com/?page=like'

    resp = opener.open(url)

    # 存储cookie
    cookie.save()


# 读取cookie
def use_cookie():
    """
    实例化
    :return:
    """
    cookie = cookiejar.MozillaCookieJar()

    # 加载Cookie文件
    cookie.load(filename)
    print(cookie)


if __name__ == '__main__':
    # get_cookie()
    use_cookie()
