myList = ["aaa", "bbb","ccc","aaa",True,300]
print(myList[4])



department = list(("CSE","IT","ECE"))
print(type(department))
department[1] = "EEE"
print(department)
department.insert(3,"MECH")
print(department)
department.append("LAW")
print(department)
myList.extend(department)
print(myList)

for i in myList:
    print(i)

numbers = [100,200,300,400]

myList.remove("LAW")
print(myList)
myList.pop(2)
print(myList)

del myList[2]
print(myList)

##del numbers
##print(numbers)




