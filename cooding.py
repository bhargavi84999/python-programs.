from nbconvert.filters import markdown2asciidoc

a=1
while(a<=5):
    print(a)
    a=a+1

a=3
while(a<=6):
    print(a*3)
    a=a+2
    a=a-1

a=2
while(a<60):
    print(a)
    a=a<<1

n=253
c=0
while(n>0):
    n=n//10
    c=c+1
    print(c*10)

n=100
while(n>10):
    print(n)
    n=n>>1

for i in range(5):
    print(i)

for i in range(4,9):
    print(i)

for i in range(7,15,1):
    print(i)

for i in range(5,11,2):
     print(i)

for i in range(9,1,-1):
    print(i)

for i in range(4,11,-1):
    print(i)

for i in range(9,3,-2):
    print(i)

for i in range(5):
    print(i)
    i=i+2
    print("hi")
    print(i)

for i in range(3):
    print(i)
    i=i*2
    i=i-1
    print(i)

m=int(input("enter your marks:"))
if m>=91 and  m<=100:
    print("a grade")
elif m>=81 and m<=90:
    print("b grade")
elif m>=71 and m<=80:
    print("c grade")
elif m>=61 and m<=70:
    print("d grade")
elif m>=51 and m<=60:
    print("e grade")
elif m>=41 and m<=50:
    print("f grade")
else:
    print("fail")

