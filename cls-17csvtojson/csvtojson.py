import csv,json
fp=open("data.csv",'r')
data=list(csv.DictReader(fp))
fp=open("chandu.json",'w')
json.dump(data,fp)
