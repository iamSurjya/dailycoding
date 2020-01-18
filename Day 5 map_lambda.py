#Day 5 Use of map() and lambda() functions

#use of map() function
def addition(n):
    return n+n


print('Called using map() functoin and a defined function')
number=[2,3,4,5]
output_list=list(map(addition,number))
print(output_list)

#use of lambda functions
print('Called using map() and lambda() function without the function')
output_list=list(map(lambda n:n+n,number))
print(output_list)
