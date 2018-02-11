# Closures

def outer():
    x = 10
    print("This is outer function")

    def inner_1():
        print("This is inner_1 function")
        return x + 1

    def inner_2():
        print("This is inner_2 function")
        return x - 1

    #inner_1()
    #return inner_1
    return inner_1, inner_2

f,f1 = outer()
print(f())
print(f1())
