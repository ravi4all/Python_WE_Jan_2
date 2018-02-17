def even(num):
    return num % 2 == 0     # True | False

numbers = []

for i in range(10,55):
    numbers.append(i)

#even_nums = []

##for num in numbers:
##    even_nums.append(even(num))

even_nums = list(filter(even, numbers))
print(even_nums)
