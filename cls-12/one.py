emp=({"eid":101},{"eid":102})
emp.insert(1,{"eid":103})
#AttributeError: 'tuple' object has no attribute 'insert'
print(len(emp))