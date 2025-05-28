myDict = {
    "name":"aaa",
    "mobile":935734953,
    "address": "no:10, aa street",
     "colors": ["red", "white", "blue"]
    }

print(myDict)
print(type(myDict))
print(myDict["colors"])
print(type(myDict["colors"]))
print(len(myDict))



print(myDict.get("address"))
print(myDict.keys())
print(myDict.values())

myDict["name"] = "bbb"   # change value
print(myDict,"myDict")


# update
myDict.update({ "mobile":12345678})
myDict.update({"age":10})
print(myDict,"After update")

# remove
myDict.popitem()
print(myDict,"After popitem")

# pop()

myDict.pop("colors")

print(myDict,"After pop")


for props in myDict:
    print(props,"for loop")










