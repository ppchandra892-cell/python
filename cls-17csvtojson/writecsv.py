import csv
fp=open("data1.csv",'w',newline="")
cw=csv.writer(fp)
cw.writerow(["eid","ename","esal"])
data=[(101,"chandu",23333),
      (102,"raju",234443)]
cw.writerows(data)
print("sucess")
fp.close()