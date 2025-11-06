#List Methods
#create
eids=[101,102,103,104,102]
#index 0   1   2   3   4
#read
#list.count() - return no of occurance of specified element

print(eids.count(102))
#list.index()-return index value of first occurance of element
print(eids.index(102))

#update
#list.append()- append element end of list.
eids.append(105)
print(eids)
#list.insert(index,element)-insert element @ specified index 
eids.insert(1,23)
print(eids)
#delete