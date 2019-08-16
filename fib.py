n=int(input("enter no of fib nos"))
count=0
a=0
b=1
print(a)
print(b)
c=[]
while count<n-2:
    summ=a+b
    c.append(summ)
    a=b
    b=summ
    print(c[count])
    count+=1
print("these are fibonicci numbers")


    
