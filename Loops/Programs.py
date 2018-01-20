# Pattern Programs

#range(lowerBound, UpperBound, Step)
#0,21,3

'''
for i in range(10):
    print('*' * i)

for i in range(10):
    print(' ' * (10-i) + '*' * (2*i + 1))
'''

for i in reversed(range(0,10)):
    print(' ' * (10-i) + '*' * (2*i + 1))
