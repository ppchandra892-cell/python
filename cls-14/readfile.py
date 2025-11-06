#read data.txt file and print
fp=open("data.txt",'r')
data=fp.read()
print(data)
fp.close()