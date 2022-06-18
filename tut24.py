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