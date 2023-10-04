data = {1 : "sreehari", 2 : "sreerag", 4 : "nandana"}
print(data)

data[5] = "tester"

print(data)

"""
clear the dictionary
"""
# data.clear()
"""
find data present in the dictionary using the key
"""
print(data.get(3))

keys = data.keys()
print(keys)

keys = ['test','test_1','test_2','test_3']
values = ['pythons','java','shell','linux']

dict_1 = dict(zip(keys, values))

print(dict_1)

del dict_1['test']

print(dict_1)


prog = {'JS': 'Atom','CS':'VS','Python':['PyCharm','Sublime'] ,'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}

print(prog)

print(prog['Java']['JSE'])