# Dictionary in Python

d1 = {
    "mumbai":"taj hotel",
    "delhi": "india gate",
    "agra":"taj mahal",
    "new york":{
        "manhattan":"empire state building",
        "brooklyn":"brooklyn bridge",
        "queens":"central park"
    }
}

print(d1)
print(d1["new york"]["manhattan"])
print(d1["delhi"])



d1["paris"] =  "eiffel tower"
print(d1)

del(d1["paris"]) # is used to delete keys from dict
print(d1)


d1["tokiyo"] = "tokiyo tower"
print(d1)

#  copy function
d2 = d1.copy()
print(d2)
del(d2["mumbai"])
print("dict 2: ",d2)
print("dict 1:", d1)

#  get function
print(d2.get("new york")) 

# update function
d2.update({"lahore":"lahori gate"})
print(d2)

# keys
dictKeys = d2.keys()
print("Keys:", dictKeys)

# items
dictItem = d2.items()
print("Items: ", dictItem)