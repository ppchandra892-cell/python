import csv
fp=open("users.csv",'r')
fp1=open("chandu.csv",'w')
data=csv.reader(fp)
data1=csv.writer(fp1)
data1.writerow(data)
""" for row in data:
    data1.writerow(row)
 """



