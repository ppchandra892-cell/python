def outer():
    print("outer function")
    def inner():
        print("iner fun")
    return inner
inn=outer()
inn()

     