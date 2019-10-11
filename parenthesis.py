def validation(string):
    stack=[]
    for i in string:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
            
        elif i==')':
            
            if stack.pop()!='(':
                return False

        elif i==']':
            
            if stack.pop()!='[':
                return False

        elif i=='}':
           
            if stack.pop()!='{':
                return False
       
    if len(stack)==0:
        return True
    else:
        return False




string=input("ENTER STRING")
print(validation(string))
