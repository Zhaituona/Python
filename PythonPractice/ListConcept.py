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

num= [12,34,5,67,88]
st1 =["selenium","java","python"]
num1 = num + st1
print(num1)
print(num1[2])
print(num1[-5])
# append method , will add value at the end
num.append(123)
print(num)
st1.append("hello")
print(st1)
num.append(6**3)
print(num)

name= ['a','b','c','d','e','f']
name[2:5]= ['A','B','C']
print(name)
name[2:5]=[]# remove added element
print(name)

# remove all the element in the list
name[:]= []
print(name )

testDate = [12,3,4,5,6,7] # length of the list
print(len(testDate))
print(len(st1))
# nested list, list inside a list
a= [1,2,3]
n = ['a','b','c']
x= [a,n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print(x[1][2])