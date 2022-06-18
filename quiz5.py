"""
Pattern Printing:
Input = Integer n; let n = 4
Booelean = True or False

True n = 4
*
**
***
****

False n = 4
****
***
**
*
"""


try:
    n = int(input("Enter the number:"))
    toggle = int(input("Enter the toggling mode 1/0:"))
    if toggle:
        for i in range(n+1):
            for j in range(i):
                print("*", end=" ")
            print()
    else:
        for i in reversed(range(n + 1)):
            for j in range(i):
                print("*", end=" ")
            print()
except Exception as e:
    print(e)
"""
for (i=1; i<=n; i++){
    for(j=0; j<i; j++){
        print(j)
    }
}
"""
"""
OUTPUT:
Enter the number:4
Enter the toggling mode 1/0:0
* * * * 
* * *
* *
*

Enter the number:4
Enter the toggling mode 1/0:1

*
* *
* * *
* * * *
"""