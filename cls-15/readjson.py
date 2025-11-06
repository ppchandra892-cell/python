#read json file and print data
#read json file and print all employees
import json
fp=open("data.json",'r')
emp_data=json.load(fp)
print(emp_data)
print(type(emp_data))