b=bytes([12,2,3,44])
b[100] #error immutable type error
for value in b:
    print(value)

