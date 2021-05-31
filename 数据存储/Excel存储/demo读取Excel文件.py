import openpyxl

# 加载Excel文件
wb = openpyxl.load_workbook('我的工作薄.xlsx')

# 获取工作表对象
# sheet = wb.active
sheet = wb['Sheet']

# 获取指定的单元格中的内容
cell = sheet['A1']

# 获取A列的所有数据
columns = sheet['A']
for i in columns:
    print(i.value)
print('-----------------------------')
# 获取特定的一行数据
row = sheet[3]
for r in row:
    print(r.value)
print('******************************')
# 获取指定间隔的数据  B列到C列
cols = sheet['B:C']
for c in cols:
    for o in c:
        print(o.value)

# 获取所有行
for s in sheet.rows:
    print(s)
