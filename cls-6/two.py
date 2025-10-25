a=10
b=[10,20,30]
c=[10,20,30]
print(id(a))
print(id(b[0]))
print(id(c[0]))
print(b[0] is c[0]) #true (address same)
print(b is c)  #false