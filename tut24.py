# Scope, Global variables


l = 20 #global scope
m = 50

def func1():
    l = 10 #Local variables
    global m # global keyword is used to give permission to access global varibales to do any updation
    m = m + 20
    print(l, m)

func1()
print(l)


x = 50
def faisal():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan()", x)
    rohan()
    print("after calling rohan()",x)

faisal()
"""
Before calling rohan() 20
after calling rohan() 20
"""
print(x) # 88


iAmGlobalToFoo = 500
def foo():
    iAmGlobalToFoo = 100
    def fizz():
        global iAmGlobalToFoo 
        iAmGlobalToFoo = 200
        iAmGlobalToFoo += 1
        print("Inside Fizz:", iAmGlobalToFoo)
    print("Before calling fizz():", iAmGlobalToFoo)
    fizz()
    print("After calling fizz():", iAmGlobalToFoo)

foo()
print(iAmGlobalToFoo)


length = 20
def rectangle():
    global length
    length = length + 40
    print(length)

print(length)
rectangle()
print(length)