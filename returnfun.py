def fun (x,y):
    print(x,y)
    return x+y
print(fun(10,20))

def fun (x,y):
    return x+y
print(fun(30,40))

def great(a,b):
    if a>b:
        return a
    else:
        return b
print((great(75,79)))

def fun(*a):
    return sum(a)
x=fun(1,3,6,7,8,9,3,4)
if x%2==0:
    print(f"even:{x}")
else:
    print(f"odd:{x}")

name=input("enter your name")
s=f"name:{name}"
print(s)

def fun5(x,y):
    print(x+y)
z=fun5
print(z(10,45))

a=10
k=f"a:{a}"
print(a)
a=30
print(k)
