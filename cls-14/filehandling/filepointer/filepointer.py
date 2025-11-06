fp=open("wish.txt",'w')
print(fp.name)#wish.txt
print(fp.writable())#true
print(fp.readable())#false
print(fp.closed)#false
fp.close()
print(fp.closed)#true