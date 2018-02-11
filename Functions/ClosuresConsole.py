Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Jan_2018\Python_WE_2\Functions\03-DynamicArguments.py 
ID : 101
Name : Ram
Age : 23
Address : xyz
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Jan_2018\Python_WE_2\Functions\03-DynamicArguments.py 
Traceback (most recent call last):
  File "C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Jan_2018\Python_WE_2\Functions\03-DynamicArguments.py", line 16, in <module>
    emp(101,"Ram",23,"xyz","abc","ijk")
TypeError: emp() takes 4 positional arguments but 6 were given
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Jan_2018\Python_WE_2\Functions\03-DynamicArguments.py 
ID : 101
Name : Ram
Age : 23
Address : ('xyz', 'abc', 'ijk')
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Jan_2018\Python_WE_2\Functions\03-DynamicArguments.py 
ID : 101
Name : Ram
Age : 23
Address : xyz
Address : abc
Address : ijk
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Jan_2018\Python_WE_2\Functions\03-DynamicArguments.py 
What do you want to update : name,age or address ? age
Enter the updated age25
Update age is 25
>>> def one():
	return "Hello","Hi","Bye","Hey"

>>> a,b,c,d = one()
>>> a
'Hello'
>>> b
'Hi'
>>> c
'Bye'
>>> d
'Hey'
>>> a,b,*c = one()
>>> a
'Hello'
>>> b
'Hi'
>>> x
>>> c
['Bye', 'Hey']
>>> a,*b,c = one()
>>> a
'Hello'
>>> b
['Hi', 'Bye']
>>> c
'Hey'
>>> def emp(name,*address,age):
	print(name,age,address)

	
>>> emp("Ram","Rohini","Kashmiri Gate","Noida",23)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    emp("Ram","Rohini","Kashmiri Gate","Noida",23)
TypeError: emp() missing 1 required keyword-only argument: 'age'
>>> def emp(name,age,*address):
	print(name,age,address)

	
>>> emp("Ram",23,"Rohini","Kashmiri Gate","Noida")
Ram 23 ('Rohini', 'Kashmiri Gate', 'Noida')
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Jan_2018\Python_WE_2\Functions\03-DynamicArguments.py 
Emp Details : {'name': 'Ram', 'age': 23, 'salary': 25000}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Functions/04-NestedFunctions.py 
This is outer function
This is inner function
11
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Functions/04-NestedFunctions.py 
This is outer function
This is inner function
11
>>> def outer():
	x = 10
	return x + 1

>>> a = outer()
>>> a
11
>>> def outer():
	x = 10
	def inner():
		return x + 1
	return inner()

>>> outer()
11
>>> a = outer()
>>> print(a)
11
>>> a
11
>>> def outer():
	x = 10
	def inner():
		return x + 2
	return inner()

>>> a
11
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Functions/05-Closures.py 
This is outer function
<function outer.<locals>.inner_1 at 0x0000021C141327B8>
>>> f()
This is inner_1 function
11
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Functions/05-Closures.py 
This is outer function
This is inner_1 function
11
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Functions/05-Closures.py 
This is outer function
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Functions/05-Closures.py", line 20, in <module>
    print(f())
TypeError: 'tuple' object is not callable
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/Functions/05-Closures.py 
This is outer function
This is inner_1 function
11
This is inner_2 function
9
>>> 
