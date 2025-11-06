#read and write
fp1=open("data.txt",'r')
fp2=open("wish.txt",'w')
data=fp1.read()
fp2.write(data)
print("new file")
fp1.close()
fp2.close()