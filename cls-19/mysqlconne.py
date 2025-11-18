import requests,json,csv,mysql.connector
try:
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    users=response.json()
    fp=open("ravi.json",'w')
    fp1=open("ramu.csv",'w',newline="")
    user_csv_t=[]
    user_json_d=[]
    for user in users:
        user_csv_t.append((user['id'],
                       user['username'],
                       user['email'],
                       user['address']['city']))
        user_json_d.append({"uid":user['id'],
                       "uname":user['username'],
                        "email":user['email'],
                        "city":user['address']['city']}) 
    dbcon=None 
    cursor=None 
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='db7'
                                  )
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
           insert into users(id,username,email,city)
           values(%s,%s,%s,%s)
           '''
    cursor.executemany(sql_st,user_csv_t)
    dbcon.commit()
    print("sucessfully created ")
    #csv
    cw=csv.writer(fp1)
    cw.writerow(["uid","uname","email","city"])
    cw.writerows(user_csv_t)
    print("sucessfully created")
    #json
    json.dump(user_json_d,fp)
    print("new json file created")
    
except mysql.connector.Error as err:
    print("err")

finally:
    fp.close()
    fp1.close()
    dbcon.close()
    cursor.close()
