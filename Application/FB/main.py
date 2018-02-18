def login():
    print("Login Now")
    
def register():
    print("Register Now")

def err_handler():
    print("Wrong Choice...")

main = True
while main:
    print("""
    1. Login
    2. Register
    3. Quit
    """)

    options = {
        "1" : login,
        "2" : register,
        }

    userChoice = input("Enter your choice : ")
    if userChoice == "3":
        main = False
    else:
        options.get(userChoice, err_handler)()
