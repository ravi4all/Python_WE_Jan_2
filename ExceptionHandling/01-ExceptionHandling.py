def exception():
    try:
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        c = a + b
        print("Add is", c)
        d = a - b
        print("Sub is", d)
        e = a / b
        print("Div is", e)
        f = a * b
        print("Mul is", f)

    except BaseException as err:
        # print("Error...")
        print(err)
        exception()

exception()