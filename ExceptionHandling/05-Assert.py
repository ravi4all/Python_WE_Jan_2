def atm():
    total_bal = 20000
    pin = int(input("Enter your PIN : "))

    withdrawAmount = int(input("Enter the amount you want to withdraw : "))
    try:
        assert (withdrawAmount < total_bal), AssertionError("Insufficient Balance")
        total_bal = total_bal - withdrawAmount
        print("Remaining bal is",total_bal)
    except AssertionError as err:
        print(err)
        atm()

atm()