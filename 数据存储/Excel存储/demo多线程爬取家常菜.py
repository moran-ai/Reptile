import threading
import time
import csv
import multiprocessing
import openpyxl
import requests
import re
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().random
}


def send_response(url):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        raise e


def parse_data(html):
    # 菜名
    names = re.findall('<p.*?class="name">.*?<a.*?>(.*?)</a>.*?</p>', html, re.S)
    for name in names[3:]:
        n = name.replace(' ', '').replace('\n', '').strip().replace('<spanclass="ellipsis-line-2">', '').replace(
            '</span>',
            '')

    # 获取食材
    shicai = re.findall('<p.*?class="ing ellipsis">(.*?)</p>', html, re.S)
    for s in shicai:
        s_ = s.replace('<span>', '').replace('</span>', '')
        ss_ = re.findall('<a.*?>(.*?)</a>', s_)

    food_url = re.findall('<p.*?class="name">.*?<a.*?href=(".*?").*?>', html, re.S)
    for url in food_url[:-1]:
        u = 'https://www.xiachufang.com' + url.replace('"', '')
    data = []
    for i in range(len(names)):

        item = {}
        name = names[i].replace(' ', '').replace('\n', '').strip().replace('<spanclass="ellipsis-line-2">', '').replace(
            '</span>', '')
        try:
            n = ','.join(re.findall('<a.*?>(.*?)</a>', shicai[i].replace('<span>', '').replace('</span>', '')))
        except:
            n = None
        url = 'https://www.xiachufang.com' + food_url[i].replace('"', '')
        # item['菜名'] = name
        # item['食材'] = n
        # item['链接'] = url
        data.append([name, n, url])
        # print(data)
        # print(data)

    # with open('家常菜.csv', 'w+',encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['菜名', '食材', '链接'])
    #     for i in data:
    #         writer.writerow(i.values())
    #         print(i)
    wb = openpyxl.Workbook()
    sheet = wb.active
    # sheet.append([name, n, url])
    for row in data:
        sheet.append(row)
        # sheet.append()
    wb.save('家常菜.xlsx')


if __name__ == '__main__':
    start_time = time.time()
    num = int(input('输入爬取的页数：'))
    for i in range(1, num):
        url = f'https://www.xiachufang.com/category/40076/?page={i}'
        # print(url)
        html = send_response(url=url)
        # 单进程
        parse_data(html)
        time.sleep(2)
        # 多线程
        # thread_k = threading.Thread(target=parse_data, args=(html,))
        # thread_k_1 = threading.Thread(target=parse_data, args=(html,))
        # thread_k_2 = threading.Thread(target=parse_data, args=(html,))
        # thread_k.setDaemon(True)
        # thread_k.start()
        # thread_k.join()
        # time.sleep(3)
        # thread_k_1.setDaemon(True)
        # thread_k_1.start()
        # thread_k_1.join()
        # time.sleep(3)
        # thread_k_2.setDaemon(True)
        # thread_k_2.start()
        # thread_k_2.join()
        # time.sleep(3)
        # 多进程
        # thread_k1= multiprocessing.Process(target=parse_data, args=(html, ))
        # # thread_k2= multiprocessing.Process(target=parse_data, args=(html, ))

    end_time = time.time()
    print(f'耗时{end_time - start_time}s')

