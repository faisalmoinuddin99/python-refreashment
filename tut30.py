# time module in python

import time

initial1 = time.time()
# print(initial1)

for i in range(150000):
    # print("Faisal bhai")
    pass
print(f"For loop took {time.time() - initial1} seconds")

k = 0
initial2 = time.time()
while k < 15:
    print("faisal bhai while")
    time.sleep(2)
    k += 1
print(f"while loop took {time.time() - initial2} seconds")


localTime = time.asctime(time.localtime(time.time()))
print(localTime) #Sun Jun 19 17:49:56 2022

