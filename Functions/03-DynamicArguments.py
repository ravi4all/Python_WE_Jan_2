# *args and **kwargs

def updateEmp():
    userChoice = input("What do you want to update : name,age or address ? ")
##    if userChoice == "name":
##        updatedName = input("Enter the updated name : ")
    updatedVal = input("Enter the updated {}".format(userChoice))
    print("Update {} is {}".format(userChoice,updatedVal))

def emp(id,name,age,*address):
    print("ID : {}".format(id))
    print("Name : {}".format(name))
    print("Age : {}".format(age))
    #print("Address : {}".format(address))

    for addr in address:
        print("Address :",addr)

#emp(101,"Ram",23,"xyz","abc","ijk")
#updateEmp()

def empDetails(**details):
    print("Emp Details :",details)

empDetails(name="Ram", age = 23, salary = 25000)
