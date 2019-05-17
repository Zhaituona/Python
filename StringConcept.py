s1 = "test Selenium"
s2 = 'Test python  z'
print(s1 + " "+ s2)
print(s1)
print(s2)
print(s1[0])
print("hello \n world")
print("hello \t world ")
print("test"*5) # multiply concepts
print(s2[0:5])
print("test" in s1 )
print("Selenium" in s1 )
print("Test" not in s2)
print("my name is %s and my age is %d" %("zaytuna",31))
s3= """test java 
test selenium
test python 
ans this is my python code """
print(s3)

print("hi i\'am zaytuna")
print("I am learning \"python\" i am happy")
s4 = "this is MY python code and I love learn python , python IS interesting"
print(s4)
print(s4.capitalize())
print(s1.capitalize())# only capitalize first letter
print(s4.count("python"))
print(s4.find("code"))
print(s2.find("python"))

print(len(s4))
print(len(s1))
print(s4.lower())
str = " hello  python "
print(str.lstrip()) # remove left space
print(str.rstrip()) # remove right space
print(max(s4))
print(max(s2))

str2 ="abcz"
print(min(str2))
print(max(str2))

str3 = "Hello Test Selenium"
print(str3.replace("Hello", "Bye"))

st4 = "java hello selenium hello python" # it will remove hello ,
st5 = st4.split("hello")
print(st5)
print(st5[2])
print(st4.upper())

st6 ="python" # can able to count from first to back , can be able to count from back to forward
print(st6[0])
print(st6[-4])

a= " test java selenium python hello"
b = " test java selenium python hello"
print(a is b) # is will check identity
print( a == b) # equal will check quality , exactly equal or not
if(a == b):
    print(" a and b are same")
else:
    print(" a is not equal b")

c= " test!"
d= " test!"
print(c is d )
print(c == d)