Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4,'Hello','Hi',10.5,True]
>>> type(a)
<class 'list'>
>>> a[3]
4
>>> a[5]
'Hi'
>>> a[-1]
True
>>> a[0:5]
[1, 2, 3, 4, 'Hello']
>>> a[:]
[1, 2, 3, 4, 'Hello', 'Hi', 10.5, True]
>>> a[0:]
[1, 2, 3, 4, 'Hello', 'Hi', 10.5, True]
>>> a[2:]
[3, 4, 'Hello', 'Hi', 10.5, True]
>>> a[:8]
[1, 2, 3, 4, 'Hello', 'Hi', 10.5, True]
>>> a[0:8:2]
[1, 3, 'Hello', 10.5]
>>> a
[1, 2, 3, 4, 'Hello', 'Hi', 10.5, True]
>>> a = [23,11,4,56,7,8,4,5,12,11,10]
>>> sorted(a)
[4, 4, 5, 7, 8, 10, 11, 11, 12, 23, 56]
>>> a
[23, 11, 4, 56, 7, 8, 4, 5, 12, 11, 10]
>>> b = sorted(a)
>>> b
[4, 4, 5, 7, 8, 10, 11, 11, 12, 23, 56]
>>> a.sort()
>>> a
[4, 4, 5, 7, 8, 10, 11, 11, 12, 23, 56]
>>> a.append(100)
>>> a
[4, 4, 5, 7, 8, 10, 11, 11, 12, 23, 56, 100]
>>> a.pop()
100
>>> a
[4, 4, 5, 7, 8, 10, 11, 11, 12, 23, 56]
>>> a.pop(2)
5
>>> a.remove(23)
>>> a
[4, 4, 7, 8, 10, 11, 11, 12, 56]
>>> a.sort(reverse = True)
>>> a
[56, 12, 11, 11, 10, 8, 7, 4, 4]
>>> tup_1 = (56, 12, 11, 11, 10, 8, 7, 4, 4)
>>> type(tup_1)
<class 'tuple'>
>>> tup_1 = 56, 12, 11, 11, 10, 8, 7, 4, 4
>>> type(tup_1)
<class 'tuple'>
>>> tup[0]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tup[0]
NameError: name 'tup' is not defined
>>> tup_1[0]
56
>>> tup_1[0:4]
(56, 12, 11, 11)
>>> a
[56, 12, 11, 11, 10, 8, 7, 4, 4]
>>> a[0] = 'Bye'
>>> a
['Bye', 12, 11, 11, 10, 8, 7, 4, 4]
>>> tup_1[0] = 'Bye'
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    tup_1[0] = 'Bye'
TypeError: 'tuple' object does not support item assignment
>>> 
