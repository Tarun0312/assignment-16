# 8. Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

print(sorted(tuple1,key=lambda a:a[1]))

