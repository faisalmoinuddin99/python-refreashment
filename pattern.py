num = int(input("Enter num how many rows you want:"))
pattern = int(input("Enter 1 or 0:"))

if pattern:
    for i in range(0,num + 1):
        print("*"*i)
else:
    for i in reversed(range(0,num + 1)):
        print("*"*i)


k=5
print(k*"f")