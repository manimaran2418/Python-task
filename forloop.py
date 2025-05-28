#print all the numbers from 1-15
for i in range (1,16):
    print(i)
    
#print odd numbers 6-29
for i in range (6,29):
    if i%2!=0:
        print(i)

#print even numbers 20-40
for i in range (20,41,2):
    print(i)

#div by 3,5,3 and 5
for i in  range (1,16):
    if i%3==0 and i%5==0:
       print('the numberis divisible by 3 and 5')
    elif i%3==0:
        print('the number is divisible by 3')
    elif i%5==0:
         print('the number is divisible by 5')
         
#print all elememt of an list
mylist=[1,2,3,4,5,6,7,8,9]
for i in mylist:
          print(i)
#calculate the sum of all the element in list
a=[1,2,3,4,5,6,7,8,9]
x=0
for i in a :
    x=x+i
    print(x)
#caluclate the sum of all numbers from 1 to 100
x=0
for i in range(1,101):
    x=x+i
print(x)

#calculate the factorial of given number
a=int(input('enter any number:'))
f=1
for i in range(1,a+1):
    f*=i
print(f)

#find maximum element in a list
a=[1,5,3,8,9,4,7]
m=a[0]
for i in a:
    if m<i:
        m=i
print(i)

#
r=10
for i in range(1,r+1):
    print('*'*i)

    










         










         


        

        
    
    
        
        
        
        
