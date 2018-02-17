# Lambda expressions

##def a(x,y):
##    return x + y
##
##lambda x,y : x + y

numbers = []
for i in range(2,101):
    numbers.append(i)

even_nums = list(filter(lambda num : num % 2 == 0, numbers))
print(even_nums)
