#create
eids={101,102,103,104}
uids=eids.copy()
print(uids)
#read
#eids.count() AttributeError: 'set' object has no attribute 'count'
#update
eids.add(108)
print(eids)
eids.update({105,106,107})
print(eids)
#delete
eids.pop()#removes 
print(eids)
eids.remove(102)
print(eids)
eids.discard()
