
a=int(input('enter any number'))
b=a
c=0
while a>0:
    d=a%10
    c=c*10+d
    a=a//10
print(c)

#
for i in range(50):
    if i%15==0:
        print('fizzbuzz',i)
    elif i%3==0:
        print('fizz',i)
    elif i%5==0:
            print('buzz',i)
#
a=5
for i in range(0,a):
    print(' ''*'*5)
#
a=5
for i in range(4):
    if i==0 or i==3:
        print('****')
    else:
        print('*    *')
        
