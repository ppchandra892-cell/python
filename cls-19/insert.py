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
           insert into employees
           values
           (101,"Rahul","rg@gmail.com","Bangalore");
           '''
    cursor.execute(sql_st)
    dbcon.commit()
    
except mysql.connector.Error as err:
    print("error")

finally:
    dbcon.close()
    cursor.close()