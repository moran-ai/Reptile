import mysql.connector

# 创建连接对象
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='itcast',
    database='python_test'
)

# 获取游标
cursor = db.cursor()

# 编写sql语句
sql = 'insert into student(id,name) values (%s,%s)'
values = (1, '张三')
# sql = "insert into student (id, name) values (2, '李四')"
# sql = f"insert into student (id, name) values ({2}, {'李四'})"
# cursor.execute(sql,values)
# cursor.execute(sql)
cursor.execute(sql, values)
db.commit()
print('插入数据成功')
