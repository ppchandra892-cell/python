#write a program script to read employeejson file and
#print no of male employees
#and no.of female employees
import json
male=0
female=0
fp=open("employee.json",'r')
employees=json.load(fp)
for emp in employees:
    if emp['gender']=="Male":
        male=male+1
    elif emp['gender']=="Female":
        female=female+1
print("femaleemp",female['ename'])
print("maleemp",male)

    
fp.close()