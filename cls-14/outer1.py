def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner
inn=outer()
inn()
print(type(inn))
inn()