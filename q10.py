# 10. Write a python program to change the first item (22) of a list within the following tuple
# to 222.
# tuple1 = (11, [22, 33], 44, 55)

tuple1=(11,[22,33],44,55)
l1=list(tuple1)
l2=[]
for e in l1:
    if(e==[22,33]):
        l2.append([222,33])
    else:    
        l2.append(e)



for e in tuple(l2):
    print(e,end=',')