
#1 positive negative
a=int(input("enter any year"))
match a%4==0:
    case True:
         print("it is a leap year")
         print("leap year")
    case False:
         print("it is not a leap year")

#2 operators
operators=input("enter any operators")
a=10
b=20
match operators:
     case'+':
        print(a+b)
     case'-':      
        print(a-b)
     case'*':
        print(a*b)   
     case'/':
        print(a/b)
#3 positive negative
a=int(input("enter any number"))
match a>0:
         case True:
              print('it is+ve')
         case False:
              print('it is -ve')

#4 vowels
a=(input("enter any letter"))
match a in 'aeiouAEIOU':
        case True:
             print('it is a vowels')
        case False:
             print('it is a constant')

#5 monts
a=input('enter the months')
match a:
    case ' jan'|' feb'|' dec':
        print ('winter')
    case'mar'|'apr'|'may':
        print ('summer')
    case' jun'|' july'|'aug':
        print ('monsoon')
    case'sep'|' oct  '|'nov':
        print ('autumn')
        
#6 grreater or lesser than
a=9
b=40
match a<b:
      case True:
          print('a is smaller')
      case False:
        print('a is not smaller')

#7
a=int(input('enter a number'))
match a%5==0 and a%3==0:
      case True:
          print('the number is divisible be 5 an 3')
      case False:
          print('the number is not divisible be 5 an 3')
match a%5==0:
      case True:
          print('the number is divisible by 5')
match a%3==0:
      case True:
          print('the number is divisible by 3')


















      
      
    
      
    
