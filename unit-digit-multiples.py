A=int(input())
if(A>0):
    x=A%10
    for i in range(1,6):
        print(x*i,end=" ")
elif(A<0):
    A=abs(A)
    y=A%10
    for j in range(1,11):
        print(y*j,end=" ")
