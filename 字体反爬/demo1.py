import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {
    'User-Agent': str(UserAgent().random)
}


def send_request():
    url = 'https://www.shixiseng.com/interns?page=1&type=intern&keyword=python'
    resp = requests.get(url=url, headers=headers)
    # print(resp.text)
    return resp.text


def parser_detail(url):
    html = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.title.text
    # print(title)
    # 公司名称
    companys = soup.select('.com_intro .com-name ')[0].text.replace('\n', '')
    # print(companys)
    # 获取薪水
    # utf-8编码
    salary = soup.select('.job_money.cutom_font')[0].text.encode('utf-8')
    # 替换
    salary = salary.replace(b'\xee\xa0\x82', b'1')
    salary = salary.replace(b'\xef\x8a\x9a', b'5')
    salary = salary.replace(b'\xee\xb7\x89', b'0')
    salary = salary.replace(b'\xee\xaf\x9e', b'2')
    salary = salary.replace(b'\xee\xbb\xb6', b'3')
    salary = salary.replace(b'\xef\x9b\x98', b'8')
    salary = salary.replace(b'\xee\xa9\x83', b'0')
    salary = salary.replace(b'\xef\x86\x9f', b'5')
    # 解码
    salary = salary.decode('utf-8')
    print(title, '----->', salary, '----->', companys)


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    offers = soup.select('.intern-wrap.intern-item')
    # print(offers[0])
    for offer in offers:
        url = offer.select('.f-l.intern-detail__job a')[0]['href']
        # print(url)
        parser_detail(url=url)


if __name__ == '__main__':
    html = send_request()
    parse_html(html)
