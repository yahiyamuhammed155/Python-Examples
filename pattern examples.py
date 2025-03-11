for row in range(0,8):
    for col in range(0,row):
        print("*",end="")
    print("")    

row=8
while row>0:
    col=0
    while col<row:
        print("*",end="")
        col=col+1
    print("")
    row=row-1  

for row in range(0,8):
    for col in range(1,row):
        print(col,end="")
    print("")    

row=8
while row>0:
    col=0
    while col<row:
        print(col,end=" ")
        col=col+1
    print("")
    row=row-1    

data=input("enter a value or 0 for quit")
while data!='0':
    print(data)
    data=input("enter a value or 0 for quit")

data=input("enter a value or 5 for quit")
while data!='5':
    print(data)
    data=input("enter a value or 5 for quit")

data=input("enter a value or z for quit")
sum=0
while data!='z':
    sum=sum+int(data)
    print(sum)
    if sum>100:
        break
    data=input("enter a value or z for quit")
sum

data=input("enter a value or a for quit")
sum=0
while data!='a':
    sum=sum+int(data)
    print(sum)
    if sum>500:
        break
    data=input("enter a value or a for quit")
sum

data=input("enter a value or 0 for quit")
while data!='0':
    if data=='8':
       data=input("enter a value or 0 for quit")
       continue
    print(data) 
    data=input("enter a value or 0 for quit")

list1=[1,2,3,4,5,6,7,8,9,10]
index=0
while index<len(list1):
    if index in [4,5,6]:
        index=index+1
        continue
    print(list1[index])
    index=index+1

list2=[21,22,23,24,25,26,27,28,29,30]
index=0
while index<len(list2):
    if index in [1,2,3]:
        index=index+1
        continue
    print(list2[index])
    index=index+1

data=range(1,101)
index=0
while index <len(data):
    if data[index] in range(50,61):
        index=index+1
        continue
    print(data[index])
    index+=1
 
data=range(1,51)
index=0
while index<len(data):
    if data[index] in range(10,20):
        index=index+1
        continue
    print(data[index])
    index+=1

data=range(1,101)
index=0
while index<len(data):
    if data[index] in range(50,61):
        index+=1
        continue
    if data[index]==81:
        break
    print(data[index])
    index+=1

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

2*3.14*1.1
3.14*1*1.1
import math
math.pi*1.1**2

fname=input("first name")
lname=input("lastname")

print(lname," ",fname)

data=input("pls enter values")
data
list4=data.split(",")
list4
tuple1=tuple(list4)
tuple1

data=input("pls enter values")
data
list2=[]
for value in data:
    list2.append (value)
list2=data.split(",")
list2
tuple2=tuple(list2)
tuple2

data=input("pls enter file name")
data
datatuple=data.split(".")[1]
datatuple

list7=["balck","white","green","blue"]
list7.pop(0)
list7.pop(3)
list7

n='5'
int(n)+int(n+n)+int(n+n+n)
