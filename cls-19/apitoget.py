
import requests
import json
import csv
import mysql.connector

try:
    # fetch data
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    # open files
    fp = open("chandu.json", 'w')
    fp1 = open("raju.csv", 'w', newline="")

    # lists for CSV and JSON
    user_csv_t = []
    user_json_d = []

    # loop through API data
    for user in users:
        user_csv_t.append((
            user['id'],
            user['username'],
            user['email'],
            user['address']['city']
        ))

        user_json_d.append({
            "uid": user['id'],
            "uname": user['username'],
            "email": user['email'],
            "city": user['address']['city']
        })

    # connect to MySQL
    dbcon = None
    cursor = None
    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db2'
    )
    print(dbcon.is_connected())

    cursor = dbcon.cursor()

    # insert data
    sql_st = '''
           insert into users(id, username, email, city)
           values(%s, %s, %s, %s)
           '''
    cursor.executemany(sql_st, user_csv_t)
    dbcon.commit()
    print("Data successfully inserted into MySQL")

    # write to CSV
    cw = csv.writer(fp1)
    cw.writerow(["uid", "uname", "email", "city"])
    cw.writerows(user_csv_t)
    print("CSV file successfully created")

    # write to JSON
    json.dump(user_json_d, fp)
    print("JSON file successfully created")

except mysql.connector.Error as err:
    print("Database error:", err)

finally:
    fp.close()
    fp1.close()
    cursor.close()
    dbcon.close()



