for i in range(1,7+1):
    if(i%3==1):
        print("A",end=" ")
    elif(i%3==2):
        print("B",end=" ")
    else:
        print("c",end=" ")

a=10
b=25
if(i%2==0):
    a=a+1
for i in range(a,b+1,4):
    print(i)

a=10
b=25
c=0
for i in range(a,b+1):
    if(i%2==0):
        c=c+1
        if(c%2==1):
            print(i,end=" ")

a=10
b=25
c=0
sum=0
count=0
for i in range(a,b+1):
    if(i%2==0):
        c=c+1
    if(i%2==1):
        sum=sum+i
        count=count+1

print(sum/count)


