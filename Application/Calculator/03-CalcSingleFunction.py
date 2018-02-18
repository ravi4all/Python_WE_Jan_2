def calc(x,y,opr):
    result = eval(x + opr + y)  # eval('1 + 4')
    print("Result is",result)

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")

    todo = {
        "1" : "+",
        "2" : "-",
        "3" : "/",
        "4" : "*"
        }

    opr = todo.get(userChoice)
    calc(num_1,num_2,opr)
    
