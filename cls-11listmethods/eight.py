eids=[101,102,103,104]
eids.pop()#remove last element of the list
print(eids)#[101, 102, 103]

eids.remove(102)#remove specified list
print(eids)#[101, 103]

eids.clear()
print(eids)#[]
del eids