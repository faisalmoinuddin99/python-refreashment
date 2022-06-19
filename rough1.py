romanNumber = {
    "I":1,
    "V": 5,
    "X": 10,
    "D": 500,
    "C": 100,
    "L": 50,
    "M":1000
}
"""

def romanToInteger(userInput):
    n = len(userInput)
    output = 0
    for i in range(0,n+1):
        if romanNumber.get(i) < romanNumber.get(i+1):
            output += romanNumber.get(i+1) - romanNumber.get(i)
            i+=1
        else:
            output = romanNumber.get(i) + romanNumber.get(i+1)
            i+=1
    return output

result = romanToInteger("III")
print(result)
"""

str = "LM"
n = len(str)
print(f"Length of str:{n}")
output = 0

for i in range(0,n):
    
    if i < n - 1 and romanNumber.get(str[i]) < romanNumber.get(str[i+1]):
        output += romanNumber.get(str[i+1]) - romanNumber.get(str[i])
        i+=1
    else:
        output += romanNumber.get(str[i])
        

print(output)
        
   

