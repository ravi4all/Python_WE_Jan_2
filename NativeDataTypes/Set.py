Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = [12,34,56,78,34,56,78,99,43]
>>> set(data)
{34, 99, 43, 12, 78, 56}
>>> set_1 = {34, 99, 43, 12, 78, 56}
>>> set_2 = {23, 56, 45, 34, 90, 76}
>>> set_1 & set_2
{56, 34}
>>> set_1 | set_2
{34, 99, 43, 12, 76, 78, 45, 23, 56, 90}
>>> str_1 = "Hello world this is python programming and python is used for machine learning"
>>> str_2 = "Python is a programming language which is good for machine learning"
>>> str_1 = str_1.lower()
>>> str_2 = str_2.lower()
>>> token_1 = str_1.split()
>>> token_1
['hello', 'world', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> token_2 = str_2.split()
>>> token_2
['python', 'is', 'a', 'programming', 'language', 'which', 'is', 'good', 'for', 'machine', 'learning']
>>> set_1 = set(token_1)
>>> set_2 = set(token_2)
>>> set_1
{'learning', 'python', 'for', 'machine', 'hello', 'world', 'is', 'used', 'this', 'and', 'programming'}
>>> set_2
{'language', 'learning', 'python', 'a', 'for', 'machine', 'good', 'is', 'programming', 'which'}
>>> set_1 & set_2
{'learning', 'python', 'for', 'machine', 'is', 'programming'}
>>> set_1 | set_2
{'python', 'good', 'world', 'programming', 'a', 'which', 'learning', 'for', 'machine', 'hello', 'is', 'used', 'this', 'and', 'language'}
>>> len(set_1 & set_2) / len(set_1 | set_2)
0.4
>>> len(set_1 | set_2)
15
>>> len(set_1 & set_2)
6
>>> 
