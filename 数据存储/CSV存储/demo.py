import csv

with open('student.csv', 'a+', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['王五', 57, 100])