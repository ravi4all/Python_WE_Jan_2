# file = open('data.txt')
# data = file.read()
# print(data)
# file.close()

with open('data.txt') as file:
    data = file.read()
    print(data)