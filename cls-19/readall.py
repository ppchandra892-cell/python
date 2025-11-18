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
            select * from employees
           '''
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    #print(employees)
    for emp in employees:
        print (emp[1])
    dbcon.commit()
    
except mysql.connector.Error as err:
    print("error")

finally:
    dbcon.close()
    cursor.close()