l=[1,2,3,4,5,6,7,8,9]
c=list(filter(lambda x:x%2==0,l))
print(c)

c=list(filter(lambda x:x%2,l))
print(c)

l=[3,5,6,7,14,32]
c=list(filter(lambda x:x%3,l))
print(c)

l=[1,2,3,44,56,23,31,16]
f=list(map(lambda x:x**3,l))
k=list(filter(lambda x:x**3%4,l))
print(f)
print(k)
si=list(filter(lambda x:x%4,map(lambda x:x**3,l)))
print(si)



