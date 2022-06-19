# Enumerate Functions | Python

lst1 = ["bhindi","aloo","chopsticks","chowmein"]

i = 0
for item in lst1:
    if i % 2 is not 0:
        print(f"Jarvis please buy {item}")
    i += 1

for index,item in enumerate(lst1):
    if index % 2 == 0:
        print(f"Jarvis please buy {index} and {item}")


paneerButterMasala = ["Paneer", "Butter","Haldi","Mirchi","Dhaniya","Adark"]

for index,item in enumerate(paneerButterMasala):
    print(f"Position: {index} {item}")

"""
Jarvis please buy aloo
Jarvis please buy chowmein
Jarvis please buy 0 and bhindi
Jarvis please buy 2 and chopsticks
Position: 0 Paneer
Position: 1 Butter
Position: 2 Haldi
Position: 3 Mirchi
Position: 4 Dhaniya
Position: 5 Adark
"""