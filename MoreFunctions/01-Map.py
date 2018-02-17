temp = [34.5,33.4,36.7,38.9,32.1]

##def tempConv(c):
##    return 9/5 * c + 32

##for t in temp:
##    print(tempConv(t))

##f_temp = list(map(tempConv, temp))
##print(f_temp)

f_temp = list(map(lambda c : 9/5 * c + 32, temp))
print(f_temp)
