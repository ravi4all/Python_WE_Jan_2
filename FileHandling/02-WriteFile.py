file = open('data_1.txt', 'w')

data = ["Hello this data is written by python script",
        "This is also some demo text",
        "Write this text in your file..."
        ]

# file.write(data)

for s in data:
    file.write(s+"\n")

file.close()