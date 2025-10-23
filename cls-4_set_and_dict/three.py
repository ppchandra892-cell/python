d1={}
emp={
     'eid':101,
	 'ename':'rahul',
	 'esal':434645
	}
#read
print(d1)
print(emp)
#how to read dict values -using key values
print(emp['eid'])
print(emp['ename'])
print(emp['loc']) #KeyError: 'loc'

#update and delete
emp['ename']="rahul gandhi"
del emp['esal']
print (emp)