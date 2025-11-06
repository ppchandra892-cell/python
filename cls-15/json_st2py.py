import json
emp_str='''
[{"eid":1,"ename":"Chas","avail":true,"grade":null},
{"eid":2,"ename":"Chilton","avail":true,"grade":null},
{"eid":3,"ename":"Hewe","avail":false,"grade":null},
{"eid":4,"ename":"Fern","avail":true,"grade":null},
{"eid":5,"ename":"Diena","avail":false,"grade":null},
{"eid":6,"ename":"Kylen","avail":true,"grade":null},
{"eid":7,"ename":"Claus","avail":true,"grade":null},
{"eid":8,"ename":"Kile","avail":false,"grade":null},
{"eid":9,"ename":"Falito","avail":false,"grade":null},
{"eid":10,"ename":"Yoshiko","avail":true,"grade":null}]'''
employees=json.loads(emp_str)
print(employees)
