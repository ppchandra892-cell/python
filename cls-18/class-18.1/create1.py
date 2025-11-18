import mysql.connector
dbcon=None
curser=None
try:
    dbcon=mysql.connector.connect(host="localhost",
                                                  user='root',
                                                  password='root',
                                                  database='db1')
    curser=dbcon.cursor()
    sql_st='''
            create table student(
            uid int,
            uname varchar(32))
           '''
    print(dbcon.is_connected())
    sql_st="insert into student (uid,uname) values(%s,%s)"
    data=[(1,"chandu"),(2,"chandra"),(3,"chan"),(4,"chamak"),(5,"chinnu"),]
    curser.executemany(sql_st,data)
    dbcon.commit()
    print("sucess fully created")   
except mysql.connector.Error as err:
    print('error')
finally:
    curser.close()
    dbcon.close()