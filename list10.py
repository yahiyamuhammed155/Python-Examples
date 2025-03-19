list5=[1,2,3,4]
len(list5)

def demo():
    print("Hello")

demo()

def demo1(name):
    print("Hello "+name)

A=demo1("HISANA")
A

def demo2(name):
    return "Hello "+name

b=demo2("pradeep")
name="pradeep"
demo2(name)
b

list10=(0,8,6,7,5,4,3,2)
len(list10)

def demo():
    print("hello")
demo()

def demo3(name):
    print("hello "+name)
demo3("yahiya")

def demo4(name):
    return "hello"+name
c=demo4("yahiya")
c
name="yahiya"
demo4(name)
name="yahiya"

def demo5():
    n='5'
    print(int(n)+int(n+n)+int(n+n+n))

demo5()

def demo6(value):
    n=str(value)
    print(int(n)+int(n+n)+int(n+n+n))

demo6(7)


def demo7(num):
    for row in range(1,num):
        for col in range(0,row):
          print(col,end=" ")
        print("")   

demo7(7)

def demo8(num):
    for value in range(0,num):
        if value%5==0:
            print(value)

demo8(150)

def demo9():
    data=input("enter a value or 0 for quit")
    while data!='0':
        if data=='8':
            data=input("enter a value or 0 for quit")
            continue
        print(data) 
        data=input("enter a value or 0 for quit")

demo9()

def demo10():
    list9=[]
    for value in range(0,101):
        if (value%3==0)(value%5==0):
            list9.append(value)
    return list9

demo10()

def demo11():
    row=8
    while row>0:
        col=0
        while col<row:
            print("*",end="")
            col=col+1
        print("")
        row=row-1  
demo11()

a=int(input("enter a value"))
b=int(input("enter a value"))
c=int(input("enter a value"))
if a==b==c:
    print(3*a)
else:
    print(a+b+c)

data="o"
if data in["a","e","i","o","u"]:
    print("vowels")
else:
    print("not vowels")

data=int(input("enter a value for 0 in quit"))
data=int(input("enter a value for 0 in quit"))
data=int(input("enter a value for 0 in quit"))
if (a==b) and (a==c):
    print("sum=0")
elif(b==a) and (b==c):
    print("sum=0")
else:
    print("sum=",a+b+c)

def demo15(): 
    data=range(1,51)
    index=0
    while index<len(data):
        if data[index] in range(10,20):
            index=index+1
            continue
        print(data[index])
        index+=1
demo15()

def demo16():
    row=8
    while row>0:
        col=0
        while col<row:
           print("*",end="")
           col=col+1
        print("")
        row=row-1  
demo16()

list1=[10,99,55,44,77]
result=sum(list1)
result
print(result)

sum=0
for value in list1:
    sum=sum+value
sum

sum=0
for value in list1:
    sum=sum*value
sum

list2=[11,12,55,73]
max=list2[0]
for value in list2:
    if max<value:
        max=value
    else:
        pass
print(max)

list1=[2,5,8,2,"yahiya",10,8,"riyas","yahiya"]
set(list1)

list5=[1]
len(list5)

list6=["yahiya","hisana",2,7,5,0,123,-33]
list7=list6
list7
list8=list6.copy()
list8

list9={11,4090,909,876,10.34-9j,6578.22,99,66,}
list10={7098,87,54,909,66,34-9j,56,99,4090}
list10.intersection(list9)

list11=[1,9,4,5,77,34,9,5,23,44,77]
list2=[]
for value in list11:
    if value not in list2:
        list2.append(value)
list2
list3=list(set(list11))
list3

list13=['abc','xyz','aba','1221']
for value in list13:
    if value[0]==value[-1]:
        print(value)

list14=[11,22,33,44,67]
for index in range(0,len(list14)):
    print(index,list14[index])

list13=['abc','xyz','aba','1221']
for value in list13:
    print(value)

def sum4(a=0,b=0):
    return a+b
sum4()

def sum5(*args):
    print(args)
    return sum(args)

sum5(12,23,45)
def sum5(*args):
    print(args)
    sum=0
    for value in args:
        sum=sum+value
    return sum
sum5(12,78,23)

def sum6(a,b):
    return a+b
sum6(23,45)

def sum7(*args):
    print(args)
    return sum (args)
sum7(6778,89,90)

def sum8(*args):
    print(args)
    sum=0
    for value in args:
        sum=sum+value
    return sum
sum8(68,5643,12)

list9=["yahiya","niyas","SHIYAS","SHARIK"]
for value in list9:
    if value.islower():
        print(value)

list10=["fayis","shibu","SALMAN","SUJITH"]

def lowercase(*list10):
    upperlist=[]
    lowerlist=[]
    for value in list10:
        if value.isupper():
            upperlist.append(value)
        else:
            lowerlist.append(value)
    return upperlist,lowerlist     

lowercase("fayis","shibu","SALMAN","SUJITH","YASAR")





