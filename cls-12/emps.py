emps={
    "eid":101,
    "ename":"cabhd",
    "esal":3444
}
print(emps.get('eid'))#101
print(emps.get('loc'))#none
for key in emps.keys():
    print(key,":",emps.get('key'))