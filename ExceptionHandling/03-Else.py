try:
    file =  open('demo.txt','r')
    data = file.read()
    file.write()

except FileNotFoundError:
    print("File Not Found")
except ValueError as err:
    print("Value Error",err)
except TypeError as err:
    print("Type Error",err)

else:
    print(data)

finally:
    print("I will always execute")
    file.close()