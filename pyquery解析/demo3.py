from pyquery import PyQuery as pq

html = '''
    <html>
        <head>
            <title>PyQuery</title>
        </head>
        <bod>
            <div id='main'>
                <a href="https://www.baidu.com/">马士兵教育</a>
                <h1>欢迎来到马士兵教育</h1>
            </div>
            <h2>Python学习</h2>
        </body>
    </html>
'''
doc = pq(html)

# 获取当前节点
print(doc('#main'))

# 获取父节点，子节点，兄弟节点
print('------- 获取父节点 ----------')
print(doc('#main').parent())
print('------- 获取子节点 ----------')
print(doc('#main').children())
print('------- 获取兄弟节点 ----------')
print(doc('#main').children().siblings())
print('------- 获取属性 ----------')
print(doc('a').attr('href'))
print('------- 获取标签的内容 ----------')
print(doc('a').text())
print(doc('a').html())
print(doc('#main').text())
