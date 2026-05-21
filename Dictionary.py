my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key2'])
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])
print(my_dict['key3'][0])
print(my_dict['key3'][0].upper())
print(my_dict['key1'])
print(my_dict['key1'])
my_dict['key1'] =my_dict['key1']-123
print(my_dict['key1'])
d={}
d['animal']='Dog'
d['answer'] = 42
print(d)
d={'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])
d={'key1':1,'key2':2,'key3':3}
print('d.keys():',d.keys())
print('d.values():',d.values())
print('d.items():',d.items())
f=lambda x:x*2
print(f)
name='this is a global name'
def greet():
    name='swamy'
    def hello():
        print('hello'+name)
    hello()
greet()
print('name:',name)
print(len(name))

