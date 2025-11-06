#read data,txt file and
#write data into new file ie wish.txt file
fp=open('wish.txt','w')
data="hii this is chandu"
fp.write(data)
print("new created sucess")
fp.close()