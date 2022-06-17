# Set in Python, it only hold unique elements

from ctypes import Union


s = set()
print(type(s))

lst = [1,5,9,10]
s = set(lst)
print(s)

newSet = set()
# Functions of Sets
"""
1) .add(element)
2) .union({element})
3) .insersection({element})
4) .len()
5) .min()
6) .max()
7) .difference()
8) .isdisjoint()
9) .remove(element)
"""
newSet.add(20)
print(newSet)

unionExample = newSet.union({50,78})
print(newSet, unionExample) # {20} {50, 20, 78}

intersectionExample = newSet.intersection({20})
print(newSet, intersectionExample) # {20} {20}

print(unionExample) # {50, 20, 78}
removeSetElement = unionExample.remove(20)
print(unionExample) # {50, 78}