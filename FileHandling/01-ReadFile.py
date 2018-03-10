file = open('data.txt','r')
# data = file.read()

# data = file.readline()

# data = file.readlines()

file.seek(10)
data = file.read(18)
print(data)

file.close()