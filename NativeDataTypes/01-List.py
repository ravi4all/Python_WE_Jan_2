Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10.6
>>> round(a)
11
>>> a = 10.4
>>> round(a)
10
>>> b = 10 + 10.5 + 'Male'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b = 10 + 10.5 + 'Male'
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> b = 10 + 10.5 + 0
>>> b
20.5
>>> b = 10 + 10.5 + 1
>>> b
21.5
>>> list_1 = [45,46,34,28,'hi','hello',10.5]
>>> list_1[0]
45
>>> list_1[5]
'hello'
>>> list_1[-1]
10.5
>>> 'hi' in list_1
True
>>> list_2 = []
>>> list_1.append(11)
>>> list_1
[45, 46, 34, 28, 'hi', 'hello', 10.5, 11]
>>> list_2.append(11)
>>> list_1
[45, 46, 34, 28, 'hi', 'hello', 10.5, 11]
>>> list_2
[11]
>>> list_2.append(15)
>>> list_2
[11, 15]
>>> list_2.append(5)
>>> list_2
[11, 15, 5]
>>> list_2.append(25)
>>> 
>>> list_2
[11, 15, 5, 25]
>>> list_2.append(21)
>>> list_2
[11, 15, 5, 25, 21]
>>> list_2.append(21,25,27,78,56)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list_2.append(21,25,27,78,56)
TypeError: append() takes exactly one argument (5 given)
>>> list_2 = []
>>> for i in range(10,50):
	list_2.append(i)

	
>>> list_2
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list_2 = []
>>> list_2 = [23,45,11,6,5,67,33,21,28]
>>> sorted(list_2)
[5, 6, 11, 21, 23, 28, 33, 45, 67]
>>> list_2
[23, 45, 11, 6, 5, 67, 33, 21, 28]
>>> list_2.sort()
>>> list_2
[5, 6, 11, 21, 23, 28, 33, 45, 67]
>>> list_2.sort(reverse = True)
>>> list_2
[67, 45, 33, 28, 23, 21, 11, 6, 5]
>>> list_2.pop()
5
>>> list_2
[67, 45, 33, 28, 23, 21, 11, 6]
>>> list_2.pop()
6
>>> list_2.pop()
11
>>> list_2
[67, 45, 33, 28, 23, 21]
>>> del list_2[3]
>>> list_2
[67, 45, 33, 23, 21]
>>> list_2 = [67, 45, 33, 23, 21,'hello','hi','bye',12.5,11.5]
>>> list_2.index('hi')
6
>>> list_2.pop(6)
'hi'
>>> list_2.remove('bye')
>>> list_2
[67, 45, 33, 23, 21, 'hello', 12.5, 11.5]
>>> list_1
[45, 46, 34, 28, 'hi', 'hello', 10.5, 11]
>>> list_2
[67, 45, 33, 23, 21, 'hello', 12.5, 11.5]
>>> list_1 + list_2
[45, 46, 34, 28, 'hi', 'hello', 10.5, 11, 67, 45, 33, 23, 21, 'hello', 12.5, 11.5]
>>> list_1.extend(list_2)
>>> list_1
[45, 46, 34, 28, 'hi', 'hello', 10.5, 11, 67, 45, 33, 23, 21, 'hello', 12.5, 11.5]
>>> list_2.append([100,101,102,103])
>>> list_2
[67, 45, 33, 23, 21, 'hello', 12.5, 11.5, [100, 101, 102, 103]]
>>> list_2[-1]
[100, 101, 102, 103]
>>> list_2[-1][0]
100
>>> list_2[-1].append([10,11,12,13,14])
>>> list_2
[67, 45, 33, 23, 21, 'hello', 12.5, 11.5, [100, 101, 102, 103, [10, 11, 12, 13, 14]]]
>>> list_2[-1][-1][0]
10
>>> list_1[-1]
11.5
>>> list_2[-1]
[100, 101, 102, 103, [10, 11, 12, 13, 14]]
>>> list_2[-1][-1]
[10, 11, 12, 13, 14]
>>> list_2[-1][-1][0]
10
>>> 
