Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Loops/Programs.py 

*
**
***
****
*****
******
*******
********
*********
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Loops/Programs.py 

*
**
***
****
*****
******
*******
********
*********
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
	print(i, end='')

	
0123456789
>>> for i in range(10):
	print(i, end=' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(10):
	print(i, end='---')

	
0---1---2---3---4---5---6---7---8---9---
>>> a = "Hello world"
>>> a[0]
'H'
>>> a[-1]
'd'
>>> a[0:10]
'Hello worl'
>>> a[0:4]
'Hell'
>>> import os
>>> os.mkdir('python_dir')
>>> 'python'+1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    'python'+1
TypeError: must be str, not int
>>> 'python'+str(1)
'python1'
>>> for i in range(10):
	os.mkdir('python_'+str(i))

	
>>> 
