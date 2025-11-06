def add(a,b):
    def inner():
        print("inner")
    return a+b,"niharika",inner
result=add(2,3)
print(result)
result[2]()
