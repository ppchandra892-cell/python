import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='db4'
                                  )
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
           insert into employees(eid,ename,email,city)
           values(%s,%s,%s,%s)
           '''
    employee=[(102,"gnana","gnaba@gmail.com","wayanad"),
            (103,"chandu","chandu@gmail.com","hyd"),
            (104,"raju","raju@gmail.com","banglore"),
            (105,"prakash","prakash@gmail.com","chennai")
            ]
    
    cursor.executemany(sql_st,employee)
    dbcon.commit()
    
except mysql.connector.Error as err:
    print("error")

finally:
    dbcon.close()
    cursor.close()