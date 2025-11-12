import requests,json,csv 
fp1=open("emp.json",'w')
fp2=open('emp.csv','w',newline="")
#Extract Data from Rest API
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()
#Transform for CSV File and json file
user_csv_data=[]
user_json_data=[]
for user in users:
    user_csv_data.append((user['id'],
                          user['username'],
                          user['email'],
                          user['address']['city']))
    user_json_data.append({"uid":user['id'],
                           "uname":user['username'],
                           "email":user['email'],
                           "city":user['address']['city']})
#load data 
#csv file #json file
cw=csv.writer(fp2)
cw.writerow(["uid","uname","email","city"])
cw.writerows(user_csv_data)
print("sucessfully created data")
#json file
json.dump(user_json_data,fp1)
print("new json file")
