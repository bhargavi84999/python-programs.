def fun3(x,y=70):
    print(x,y)
    print(x+y)
fun3(30)

def fun4(x=10,y=70,z=50):
    print(x,y,z)
    print(x+y+z)
fun4(70,70,70)
fun4()

def fun(*a):
    print(a)
    print(*a)
fun(10,10,70,40,60)

def fun2(**b):
    print(b)
fun2(a=75,b=30,c=40,d=70)

def fun5(*a,**b):
    print(a,b,sep="\n")
    fun5(10,7,1,7,c=70,a=30,b=65)

def fun6(*a):
    print(sum(a))
fun6(1,7,8,25,30,60,70)

def fun7(*a):
   i=0;s=0;
   while i<len(a):
      if a[i]%2==0:
         s+=a[i]
      i+=1
   print(s)
fun7(1,7,8,25,30,60,70)

def fun(*a):
    print(sum(a[::2]))
    a[1::2]
fun(1,2,3,4,7,9)
