import requests,json
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp_data.json()
with open("user.json",'w') as fp:
    json.dump(users,fp)
    print("new file created")