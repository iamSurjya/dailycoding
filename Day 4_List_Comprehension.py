import math

#declare lists
input_list=[2,3,4,5]
output_list=[]

#List Traversal using a for loop
print('Using For loop')
for number in input_list:
    output_list.append(math.pow(number,2))
print(output_list)

#List Comprehension
print('Using List Comprehension')
output_list=[math.pow(number,2) for number in input_list]
print(output_list)
