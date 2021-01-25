#1
def a():
    return 5
print(a())
#P:5
#A:5

#2
def a():
    return 5
print(a()+a())
#P:10
#A:10

#3
def a():
    return 5
    return 10
print(a())
#P:5
#A:5

#4
def a():
    return 5
    print(10)
print(a())
#P:5
#A:5

#5
def a():
    print(5)
x = a()
print(x)
#P:5
#A:5,none

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#P:3,5
#A:3,5

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#P:none
#A:25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#P:100,10:
#A:100,10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#P:7,14,21
#A:7,14,21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#P:8
#A:8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#P:500,300,300
#A:500,500,300,500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#P:500,500,300,500
#A:500,500,300,500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#P:500,500,300,300
#A:500,500,300,300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#P:1,2,3
#A:1,3,2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#P:1,3,3,1
#A:1,3,5,10