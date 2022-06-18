f = open("faisal.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())

f.close()

"""
f.seek(0) ---> pointer will go to first line
f.tell() ---> pointer tells the current line
"""