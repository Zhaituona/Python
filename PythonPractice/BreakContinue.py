name = "zaytuna"
for i in name:
    print (i)
    if(i == "t"): # it will break the loop where the condition meat
        break

print("***********")

name = "ElzatMirzat"
for i in name:
    print(i)
    if(i == "M"):
        continue

print("************")

str = ["java","python","C sharp","ruby"]
for l in range(len(str)):
    print(str[l])
    if(str[l]== "python"):
        print(" I found python")
        continue

print("***********")
language = ["English","France","Germany","Uyghur","Spanish"]
flag = False
for index in range(len(language)):
    print(language[index])
    if(language[index]== "Germany"):
        print(" I hope I can learn Germany")
        flag = True
        break
if(flag):
    print(" Hey I like Germany")