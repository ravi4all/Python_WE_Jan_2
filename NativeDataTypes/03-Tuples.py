Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup = (1,2,3,4,5,6,7,10)
>>> tup = (1,2,3,4,5,6,7,10,'hi','hello')
>>> tup[0]
1
>>> tup[-1]
'hello'
>>> tup[0:5]
(1, 2, 3, 4, 5)
>>> tup[0] = 'Hi'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tup[0] = 'Hi'
TypeError: 'tuple' object does not support item assignment
>>> 
