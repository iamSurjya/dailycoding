#Python Code Sort vs Sorted

#sorted()
#list of integers
L=[4,1,2,3,5]
print('Sorted list')
#Sorting the list
print(sorted(L))
#demonstrate that original list was not updated
print('Original list')
print(L)

#sort()
#list of integers
print('Original list')
L1=[4,1,2,3,5]
print(L1)
#Sorting the list
L1.sort()
print('Sorted list')
print(L1)
#demonstrate that Original list was updated
print('Original list')
print(L1)
