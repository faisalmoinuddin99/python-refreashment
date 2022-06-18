# Anonymous | Lambda functions

def minusfun(x,b):
    return x - b

result = minusfun(10,5)
print(result) # 5

# lambda functions

lambdaMinus = lambda x,y: x - y
print(lambdaMinus(5,3)) # 2

def a_first(a):
    return a[0]

todoList = [[10,14],[5,6],[2,23]]
todoList.sort(key=lambda a: a[1])
print(todoList) # [[5, 6], [10, 14], [2, 23]]