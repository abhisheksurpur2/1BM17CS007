dashes=6
rows=int(input("Enter no of rows"))

for i in range(rows//2):
    print("- "*rows)
    print("| | | |")
    
if rows%2!=0:
    print("- "*rows)
   
    
