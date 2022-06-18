# Functions in Python

def average(a,b):
    """
    This is the function which is used to calculate average of two numbers
    """
    return (a + b) / 2

avg = average(5,7)
print(average.__doc__) # Doc String
print(f"Average is: {avg}")

