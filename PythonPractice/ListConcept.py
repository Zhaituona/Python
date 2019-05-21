score= [12,34,67,90,89]
print(score)
print(score[0])
print(score[-4])# this is concept for slicing, it has reverse order , -1,-2,-3,-4,-5
print(score[1:3])

# for create a duplicate copy of list
print(score[:])
print(score+ [1,2,3])
print(score +["a","b","c"])

# in python list is mutable , can be modified
number =[1,2,3,4,5,6]
number[2]=23
print(number)
number[2:4]=(34,56)
print(number)