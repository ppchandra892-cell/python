#read using load and write using dump
import json
fp=open("data.json",'r')
fp1=open("emp.json",'w')
empdata=json.load(fp)
print(empdata)
json.dump(empdata,fp1)
print("new json file is created")
fp.close()
fp1.close()
