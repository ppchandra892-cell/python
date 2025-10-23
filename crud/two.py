#create
enames=["ravi","raju","ramu"]
#read
print(enames)
print(type(enames))
#how to read list elements using indexing
print(enames[0])
print(enames[2])
#update
enames[3]="ramuuu"
print (enames) #IndexError: list assignment index out of range
#delete
del enames[3]
print (enames)