Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> emp = {'id':101,'name':'Ram','age':25,'dept':'IT'}
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp['salary'] = 15000
>>> emp['address'] = 'xyz'
>>> emp
{'id': 101, 'name': 'Ram', 'age': 25, 'dept': 'IT', 'salary': 15000, 'address': 'xyz'}
>>> emp['name']
'Ram'
>>> emp.keys()
dict_keys(['id', 'name', 'age', 'dept', 'salary', 'address'])
>>> emp.values()
dict_values([101, 'Ram', 25, 'IT', 15000, 'xyz'])
>>> for data in emp:
	print(data)

	
id
name
age
dept
salary
address
>>> for data in emp.values():
	print(data)

	
101
Ram
25
IT
15000
xyz
>>> for data in emp.items():
	print(data)

	
('id', 101)
('name', 'Ram')
('age', 25)
('dept', 'IT')
('salary', 15000)
('address', 'xyz')
>>> data = [{'id':101,'name':'Ram','age':25,'dept':'IT'},{'id':102,'name':'Aman','age':35,'dept':'IT'},{'id':103,'name':'Shyam','age':32,'dept':'HR'},{'id':104,'name':'Mohan','age':26,'dept':'Marketing'},{'id':105,'name':'Ankit','age':38,'dept':'Sales'}]
>>> data = []
>>> emp_data = {}
>>> emp_data['name'] = 'Ram'
>>> emp_data['age'] = 17
>>> emp_data['dept'] = 'IT'
>>> data.append(emp_data)
>>> data
[{'name': 'Ram', 'age': 17, 'dept': 'IT'}]
>>> data = [{'id':101,'name':'Ram','age':25,'dept':'IT'},{'id':102,'name':'Aman','age':35,'dept':'IT'},{'id':103,'name':'Shyam','age':32,'dept':'HR'},{'id':104,'name':'Mohan','age':26,'dept':'Marketing'},{'id':105,'name':'Ankit','age':38,'dept':'Sales'}]
>>> data[0]
{'id': 101, 'name': 'Ram', 'age': 25, 'dept': 'IT'}
>>> data[1]
{'id': 102, 'name': 'Aman', 'age': 35, 'dept': 'IT'}
>>> for i in range(len(data)):
	print(data[i]['id'])

	
101
102
103
104
105
>>> for i in range(len(data)):
	print(data[i]['age'])

	
25
35
32
26
38
>>> data[2]['name']
'Shyam'
>>> for i in data:
	print(i)

	
{'id': 101, 'name': 'Ram', 'age': 25, 'dept': 'IT'}
{'id': 102, 'name': 'Aman', 'age': 35, 'dept': 'IT'}
{'id': 103, 'name': 'Shyam', 'age': 32, 'dept': 'HR'}
{'id': 104, 'name': 'Mohan', 'age': 26, 'dept': 'Marketing'}
{'id': 105, 'name': 'Ankit', 'age': 38, 'dept': 'Sales'}
>>> sorted(data)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sorted(data)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> sorted_data = sorted(data, key = lambda x : x['age'])
>>> sorted_data
[{'id': 101, 'name': 'Ram', 'age': 25, 'dept': 'IT'}, {'id': 104, 'name': 'Mohan', 'age': 26, 'dept': 'Marketing'}, {'id': 103, 'name': 'Shyam', 'age': 32, 'dept': 'HR'}, {'id': 102, 'name': 'Aman', 'age': 35, 'dept': 'IT'}, {'id': 105, 'name': 'Ankit', 'age': 38, 'dept': 'Sales'}]
>>> list(filter(lambda x : x['id'] == 104, data))
[{'id': 104, 'name': 'Mohan', 'age': 26, 'dept': 'Marketing'}]
>>> 
