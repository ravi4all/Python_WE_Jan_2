Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def tempConv(c):
	return 9/5 * c - 32

>>> temp = [34.5,29.3,36.7,34.5,33.9]
>>> for t in temp:
	tempConv(t)

	
30.1
20.740000000000002
34.06
30.1
29.019999999999996
>>> def tempConv(c):
	return 9/5 * c + 32

>>> for t in temp:
	tempConv(t)

	
94.1
84.74000000000001
98.06
94.1
93.02
>>> map(tempConv, temp)
<map object at 0x000001EF409907F0>
>>> list(map(tempConv, temp))
[94.1, 84.74000000000001, 98.06, 94.1, 93.02]
>>> def even(num):
	return num % 2 == 0

>>> numbers = []
>>> for i in range(12,55):
	numbers.append(i)

	
>>> numbers
[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
>>> for n in numbers:
	even(n)

	
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
>>> def even(num):
	if num % 2 == 0:
		return num

	
>>> eveb_nums = []
>>> even_nums = []
>>> for n in numbers:
	even_nums.append(even(n))

	
>>> even_nums
[12, None, 14, None, 16, None, 18, None, 20, None, 22, None, 24, None, 26, None, 28, None, 30, None, 32, None, 34, None, 36, None, 38, None, 40, None, 42, None, 44, None, 46, None, 48, None, 50, None, 52, None, 54]
>>> list(map(even, numbers))
[12, None, 14, None, 16, None, 18, None, 20, None, 22, None, 24, None, 26, None, 28, None, 30, None, 32, None, 34, None, 36, None, 38, None, 40, None, 42, None, 44, None, 46, None, 48, None, 50, None, 52, None, 54]
>>> list(filter(even, numbers))
[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54]
>>> lambda x=12,y=15 : x + y
<function <lambda> at 0x000001EF4098D6A8>
>>> func_1 = lambda x=12,y=15 : x + y
>>> func_1
<function <lambda> at 0x000001EF409937B8>
>>> func_1()
27
>>> lambda : print("Hello world")
<function <lambda> at 0x000001EF4098D6A8>
>>> map(lambda c : 9/5 * c + 32, temp)
<map object at 0x000001EF40990320>
>>> list(map(lambda c : 9/5 * c + 32, temp))
[94.1, 84.74000000000001, 98.06, 94.1, 93.02]
>>> list(filter(lambda num : num % 2 == 0, numbers))
[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54]
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/MoreFunctions/01-FilterMapLambda.py 
94.1
92.12
98.06
102.02
89.78
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/MoreFunctions/01-FilterMapLambda.py 
94.1
92.12
98.06
102.02
89.78
[94.1, 92.12, 98.06, 102.02, 89.78]
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/MoreFunctions/01-FilterMapLambda.py 
[94.1, 92.12, 98.06, 102.02, 89.78]
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Jan_2018/Python_WE_2/MoreFunctions/01-FilterMapLambda.py 
[94.1, 92.12, 98.06, 102.02, 89.78]
>>> 
