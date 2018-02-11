# Nested Functions

#x = 10
def outer():
    x = 10
    print("This is outer function")

    def inner_1():
        print("This is inner function")
        return x + 1

    def inner_2():
        return x - 1

    #a = inner()
    #print(a)
    return inner()

#inner()
a = outer()
#a = 11
print(a)

def func_1():
    print("This is function_1")
