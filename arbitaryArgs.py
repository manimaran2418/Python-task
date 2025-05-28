def myFuc(*values):
    print(values)

myFuc(10,20,30,40)


def display(**data):
    print(data)
    print("Student name is ",data["name"])


display(name= "bhuvan",age=17)

studentData = [
    {"name": "aaa", "age":34},
    {"name": "bbb", "age":4}
    ]

print(studentData)
