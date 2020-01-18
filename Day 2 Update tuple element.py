#Python Code to update an tuple.

#creating a tuple
t1=(1,3,4,5)

print('Original tuple')
print(t1)

#trying to update a tuple
#t1[0]=7 #If you try to update the tuple directly it will throw error.

#Work around to update an tuple
L1=list(t1) #Convert the tuple into a list
L1[0]=7 #update the element as needed
t1=tuple(L1) #Convert the list back to tuple

#demonstate that the tuple was updated.
print('updated tuple')
print(t1)
