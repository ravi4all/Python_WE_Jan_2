Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> def knn(x,y):
	return math.sqrt(sum(pow(x-y,2)))

>>> knn(12,5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    knn(12,5)
  File "<pyshell#4>", line 2, in knn
    return math.sqrt(sum(pow(x-y,2)))
TypeError: 'int' object is not iterable
>>> x = [2,5,6,7,8]
>>> y = [6,7,3,4,5]
>>> knn(x,y)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    knn(x,y)
  File "<pyshell#4>", line 2, in knn
    return math.sqrt(sum(pow(x-y,2)))
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> math.sqrt(sum(pow(i-j,2) for i,j in zip(x,y) ))
6.855654600401044
>>> def knn(x,y):
	return math.sqrt(sum(pow(i-j,2) for i,j in zip(x,y)))

>>> knn(x,y)
6.855654600401044
>>> def temp
SyntaxError: invalid syntax
>>> def temp_conv(c):
	return 9/5 * c + 32

>>> temp = [34.5,33.6,32.7,36.8,39.8]
>>> for t in temp:
	temp_conv(t)

	
94.1
92.48
90.86000000000001
98.24
103.64
>>> list(map(temp_conv, temp))
[94.1, 92.48, 90.86000000000001, 98.24, 103.64]
>>> list_1 = []
>>> for i in range(0,25):
	list_1.append(i)

	
>>> list_1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
>>> list_1 = [i for i in range(0,25)]
>>> list_1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
>>> list_1 = []
>>> for i in range(0,25):
	if i%2 == 0:
		list_1.append(i)

		
>>> list_1
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
>>> list_1 = [i for i in range(0,25) if i % 2 == 0]
>>> list_1
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
>>> dict_1 = {x : [ x**x for x in range(0,10)]}
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict_1 = {x : [ x**x for x in range(0,10)]}
TypeError: unhashable type: 'list'
>>> dict_1 = {a : [a**a for a in range(0,10)]}
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict_1 = {a : [a**a for a in range(0,10)]}
NameError: name 'a' is not defined
>>> dict_1 = {[a : [a**a for a in range(0,10)]]}
SyntaxError: invalid syntax
>>> dict_1 = {'a' : [a**a for a in range(0,10)]}
>>> dict_1
{'a': [1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]}
>>> dict_1 = {'a' : [a**2 for a in range(0,10)]}
>>> dict_1
{'a': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]}
>>> dict_1 = {a : a**2 for a in range(0,10)}
>>> dict_1
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> names = ['Ram','Shyam','Ravi']
>>> dict_1 = {'name' : name for name in names}
>>> dict_1
{'name': 'Ravi'}
>>> for name in names:
	print(name)

	
Ram
Shyam
Ravi
>>> name
'Ravi'
>>> 
