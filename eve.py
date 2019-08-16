n=int(input("enter numbers & -1 to stop"))
c=[]
while n!=-1:
    c.append(n)
    n=int(input())
print("even numbers among enterd are: ")
for i in c:
    if i%2==0:
        print(i)
    
