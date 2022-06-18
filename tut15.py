# Break and Continue in Python

i = 1

while i <= 10:
    # print(f"2 * {i} = {2 * i}")
    i += 1

"""
OUTPUT: 
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
"""

i = 0
while 1:
    if i+1 < 5:
        i += 1
        continue # ignore below statements
    print(i, end=" ")
    
    if i == 30:
        break # stop the loop
    i += 1

# 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 