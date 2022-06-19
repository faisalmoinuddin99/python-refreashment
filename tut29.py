# *args and **kwargs


def fun1(normal, *args, **kwargs):
    print(f"I am normal {normal} argument")
    for i in args:
        print(f"Vegetables are: {i}", end=" ")

    for key in kwargs:
        print(f"Name: {key}")

veg = ["bhindi","aaloo","matter","adrak","limbo","dhaniya"]
roles = {
    "faisal": "CEO",
    "rahul": "Manager",
    "shivam": "waiter"
}


fun1("faisal",*veg,**roles)