##def myFunction(msg,msg2):
##    print(msg)
##    print(msg2)
##
##myFunction("welcome","demo")

##a = 10
##b =20




##a = int(input("Enter a value: "))
##b = int(input("Enter b value: "))
##def addition(n1,n2):
##    c = n1 + n2
##    print(c)
##
##addition(a,b)


##a = int(input("Enter a value: "))
##b = int(input("Enter b value: "))
##def addition(*num):
##    c = a + b
##    print(c)
##    
##addition(20,30,34,97,293)

# local scope

##name = "bbb"  # global
##def myFunc():
##    name = "aaa"   # local scope
##    print(name,"inside the function")
##
##myFunc()
##print(name,"outside the function")

def display(msg):
    print(msg,"before return")
    return msg
    print(msg,"after return")

print(display("hello"))










