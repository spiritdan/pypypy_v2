import csv

csv_file=open('demo.csv','w',newline='')
writer=csv.writer(csv_file)
writer.writerow(['银河护卫队','7.0'])
writer.writerow(['复仇者联盟','8.1'])

csv_file.close()
import csv
csv_file=open('demo.csv','r',newline='')
reader=csv.reader(csv_file)
for row in reader:
    print(row)