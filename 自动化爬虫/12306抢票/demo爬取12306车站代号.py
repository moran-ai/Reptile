import requests
import re
import openpyxl
from fake_useragent import UserAgent

headers = {
    'User-Agent': str(UserAgent().random)
}
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9186'


def get_station():
    """
    获取车站代码
    :return:
    """
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    # print(resp.text)
    # 中文在正则表达式中的范围  ^[\u4E00-\u9FA5]+$
    # 获取所有车站和车站代号
    stations = re.findall('([\u4E00-\u9FA5]+)\|([A-Z]+)', resp.text)
    # print(stations)
    return stations


def save(lst):
    """
    将车站代码放入excel表格中
    :param lst:
    :return:
    """
    wb = openpyxl.Workbook()  # 创建一个工作薄对象
    ws = wb.active  # 使用活动表
    for iten in lst:
        ws.append(iten)  # 添加数据到excel中
    wb.save('车站代号.xlsx')


if __name__ == '__main__':
    lst = get_station()
    save(lst)
