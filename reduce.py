from functools import reduce
l=[1,2,3,4,5,6,7]
a=(reduce(lambda x,y:x+y,l))
print(a)

st=['.','j','o','i','n',',']
k=reduce(lambda x,y:x+y,st)
print(k)

l=[1,2,3,6,7,8,9,4,3]
k=reduce(lambda x,y:x if x>y else y,l)
print(k)

from functools import reduce
c = [0, 20, 30, 40]
k = list(map(lambda x: (x * 9/5) + 32, c))
l = list(filter(lambda x: x % 3 == 0, c))
s = reduce(lambda x, y: x + y, c)

print(k)
print(l)
print(s)

from functools import reduce

c=[0,20,30,40]
print(list(map(lambda x:(x*9/5)+32,c)), list(filter(lambda x:x%3==0,c)), reduce(lambda x,y:x+y,c))