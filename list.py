my_list = [1,2,3]
my_list = ['A string',23,100,232,'o']
print('len(my_list): ',len(my_list))
my_list =['one','two','three',4,5]
print('my_list[0] ',my_list[0])
print('my_list[1:]',my_list[1:])
print('my_list[:3]',my_list[:3])
my_list + ['new item']
print('my_list',my_list)
my_list = my_list + ['add new item permanently']
print('my_list',my_list)
l=[1,2,3]
l.append('append mel')
print('l: appended',l)
l.pop(0)
print('l: pop',l)
new_list = ['a','e','x','b','c']
print('new_list',new_list)
new_list.reverse()
print('new_list: reversed: ',new_list)
new_list.sort()
print('new_list:sorted: ',new_list)
list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]
matrix = [list_1,list_2,list_3]
print('matrix: ',matrix)
print( matrix[0])
print(matrix[0][0])
firt_col = [row[0] for row in matrix]
print(firt_col)
file = open("example.txt","r")
file.close()
with open("example.txt","r") as file:
    content = file.read()
    print(content)
with open("example.txt","r") as file:
    line = file.readline()
    print(line)
with open("example.txt","r") as file:
    line = file.readlines()
    print(line)
import keyword
print("python keywords:")
print(keyword.kwlist)
my_variable = 10
MyVariable = 20
_var123 = 30
print("my_variable:",my_variable)
print("MyVariable:",MyVariable)
print("_var123:",_var123)
#2ndVar = 40
#my_variable = 50
#for = 60
print('1>2:',1>2)
print('1<2:',1<2)
print('1<=4:',1<=4)
print('1>=1:',1>=1)
print('1==1:',1==1)
print('1=="1":',1=="1")
print('"hi" == "bye":',"hi" == "bye")
print('1 !=2:',1 !=2)
print('(1>2) and (2<3):',(1>2) and (2<3))
print('(1>2) or (2<3):',(1>2) or (2<3))
print('(1==2) or (2==3) or (4==4):',(1==2) or (2==3) or(4==4))
if 1<2:
    print('Yep!')
if 1<2:
    print('yep!')
if 1<2:
    print('first')
else:
    print('last')
if 1==2:
    print('first')
elif 3==3:
        print('middle')
else:
    print('last')
seq=[1,2,3,4,5]
for item in seq:
    print(item)
for item in seq:
    print('Yep')
for jelly in seq:
    print(jelly+jelly)
ages= {"Sam":3,"Frank":4,"Dan":29}
for key in ages:
    print("This is the key")
    print(key)
    print(" This is the value")
    print(ages[key])
    print("\n")
mypairs = [(1,10),(3,30),(5,50)]
for tup in mypairs:
    print(tup)
for item1,item2 in mypairs:
    print(item1)
    print(item2)
i= 1
while i<10:
    print('i is: {}'.format(i))
    i=i+1
print('range(5):',range(5))
print('list(range(5)): ',list(range(5)))
for i in range(5):
    print(i)
x=range(1,10)
print(x)
range(0,10,2)
x=[1,2,3,4]
out=[]
for item in x:
    out.append(item**2)
print(out)
[item**2 for item in x]


