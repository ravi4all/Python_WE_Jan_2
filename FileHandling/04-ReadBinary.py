with open('Football.png', 'rb') as file:
    data = file.read()
    print(data)

with open('Fooball_1.png','wb') as file_2:
    file_2.write(data)