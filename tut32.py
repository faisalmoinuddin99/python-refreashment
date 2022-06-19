# How import statement works in Python

import time as t
import sys
import file1 as f

print(t.__doc__)
print(sys.path)
print(f.a) # 10

greet = f.greetInEnglish("faisal")
print(greet)
