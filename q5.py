# 5. Write a python program to check if all items in the tuple are the same.

t1=tuple([eval(e) for e in input("Enter tuple: ").split(',')])
i=0
while(i<len(t1)):
    if(t1[0]!=t1[i]):
        print("All the items in tuple are not same")
        break
    i+=1
else:
    print("All the items in tuple are same")
    
