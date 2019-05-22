x = int(input("please enter valid input x"))
if(x <0):
    print("x is negative number")
elif(x >0):
    print("x is positive number")
elif(x==0):
    print("x is equal to zero ")
else:
    print("x is not defined ")

if True:
    print("PASS")
else:# dead code , never come inside
     print("FAIL")


a = 100
b= 200
c= 400
if  a >b and a >c:
    print(" a is the biggest number")
elif b>c:
    print("b is the biggest number")
elif a<c:
    print("c is the biggest number")

y = int(input("please enter value of y "))
if(y >0):
    print("y is positive number ")
print(y)

total= int(input("please enter total value"))
if(total< 100):
    total = total + 20
elif(total>= 100 and total <= 400):
    total= total + 100
else:
    total = total+ 200

print("total=" + str(total)) # this is called str method
print(f'{"total value ="}{total}') # this is called f String formula

print(total) # must put in the specific line