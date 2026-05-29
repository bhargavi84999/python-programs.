l=[23,21,27,28,44,46]
a=sorted(l,key=lambda x:x%7,reverse=True)
print(a)

a=sorted(l,key=lambda x:x%7,reverse=False)
print(a)

l=[21,3,2,5,22,6,32]
b=sorted(l,key=lambda x:x%3)
print(b)

from functools import reduce
l=[7,8,6,3]
k=reduce(lambda x,y:x+y,l,10)
print(k)