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

# 编写sql语句 更新表数据
# sql = 'update student set name="好" where id=1'

# 删除数据
sql = 'delete from student where id=1;'

# 插入多条数据
cursor.execute(sql)
db.commit()
print('删除数据成功')
