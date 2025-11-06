def calc():
    print("outer function")
    def add():
        print("addition")
    def mul():
        print("mul")
    return add,mul
inner=calc()
print(type(inner))
inner[0]()
inner[1]()
