data = [{'Name':"Ram",'Age':24,'Company':'HCL', 'dept':'IT'},
        {'Name':"Shyam",'Age':28,'Company':'HCL', 'dept':'HR'},
        {'Name':"Anuj",'Age':22,'Company':'TCS', 'dept':'IT'},
        {'Name':"Shubham",'Age':23,'Company':'Wipro', 'dept':'Data Analyst'},
        {'Name':"Mayank",'Age':24,'Company':'TCS', 'dept':'HR'},
        {'Name':"Vivek",'Age':32,'Company':'Infosys', 'dept':'Network Analyst'},
        {'Name':"Raju",'Age':31,'Company':'IBM', 'dept':'Tech Support'},
        {'Name':"Bhanu",'Age':27,'Company':'TCS', 'dept':'BPO'},]


##def show(emp = {'name':'ram','age':23}):
##    return emp['Age'] > 25
##
###print(show(data))
##for x in data:
##    print(show(x))

#new_data = list(filter(lambda x : x['Age'] > 25, data))
#print(new_data)

new_data = list(filter(lambda x : x['Company'] == 'HCL', data))
for i in new_data:
    print(i)
