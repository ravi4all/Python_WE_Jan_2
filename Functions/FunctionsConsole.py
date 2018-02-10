Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def one():
	print("Function one...")

	
>>> def two():
	print("Function two...")

	
>>> x = {"1" : one(), "2" : two()}
Function one...
Function two...
>>> x = {"1" : one, "2" : two}
>>> x.get("1")
<function one at 0x0000012415DBD6A8>
>>> x.get("1")()
Function one...
>>> eval('12+4')
16
>>> one()
Function one...
>>> print(one())
Function one...
None
>>> def add(x,y):
	return x + y

>>> add(12,11)
23
>>> x = add(12,11)
>>> type(x)
<class 'int'>
>>> def calc(x,y):
	return x + y, x-y, x/y, x*y

>>> res = calc(12,5)
>>> res
(17, 7, 2.4, 60)
>>> i,j,k,l = calc(12,5)
>>> i
17
>>> j
7
>>> k
2.4
>>> l
60
>>> a,b,c = calc(12,5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a,b,c = calc(12,5)
ValueError: too many values to unpack (expected 3)
>>> a,b,*c = calc(12,5)
>>> a
17
>>> b
7
>>> c
>>> c
[2.4, 60]
>>> a,b,*c = calc(12,5)
>>> a
17
>>> b
7
>>> c
[2.4, 60]
>>> a,*b,c = calc(12,5)
>>> a
17
>>> b
[7, 2.4]
>>> c
60
>>> a,b,c,d,e = calc(12,5)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a,b,c,d,e = calc(12,5)
ValueError: not enough values to unpack (expected 5, got 4)
>>> 
