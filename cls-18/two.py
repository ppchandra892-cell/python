try:
    a=int(input("enter a first number:"))
    b=int(input("enter a  second number:"))
    print(a/b)
except ValueError as error:
    print("enter integer only")
except ZeroDivisionError as zero:
    print("cam not dividion by zero")
print ("gm")
