def add(x,y):
    print("Addition is",x+y)

def sub(x,y):
    print("Subtraction is",x-y)

def div(x,y):
    print("Divison is",x/y)

def mul(x,y):
    print("Multiplication is",x*y)

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    todo = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul
        }

    todo.get(userChoice)(num_1,num_2)

    #result = 0

##    if userChoice == "1":
##        add(num_1,num_2)
##    elif userChoice == "2":
##        sub(num_1,num_2)
##    elif userChoice == "3":
##        div(num_1,num_2)
##    elif userChoice == "4":
##        mul(num_1,num_2)
##    else:
##        print("Wrong choice...")
