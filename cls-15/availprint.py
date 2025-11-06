#read json and print avail employees
import json
fp=open("data.json",'r')
employees=json.load(fp)
print(len(employees))#10
print(type(employees))#<class 'list'>
for emp in employees:
    if emp['avail']==True:
        print(emp['ename'])

fp.close()