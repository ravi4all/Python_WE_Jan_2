def atm():
    total_bal = 20000
    pin = int(input("Enter your PIN : "))

    withdrawAmount = int(input("Enter the amount you want to withdraw : "))
    try:
        if withdrawAmount > total_bal:
            raise ValueError("Insufficient Balance")
        else:
            total_bal = total_bal - withdrawAmount
            print("Remaining bal is",total_bal)
    except ValueError as err:
        print(err)
        atm()

atm()