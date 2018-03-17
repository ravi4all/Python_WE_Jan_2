try:
    file =  open('demo.txt','r')
    data = file.read()
except FileNotFoundError:
    print("File Not Found")
except ValueError as err:
    print("Value Error",err)
except TypeError as err:
    print("Type Error",err)
finally:
    print("I will always execute")
    file.close()