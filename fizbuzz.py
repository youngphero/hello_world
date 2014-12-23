#!/usr/bin/python3


print("Here is my first project :-) yay")


print ('Please enter a number')    
x= input('---->')

try:
     x=int(x)
except:
     print ('I asked you to enter a number')
     
else:
    
    if x <0:
        print('Please enter a number greater than ZERO') 
 
    else:  
     
      n=1
      while n<x:
          if n%3== 0 and n%5 !=0:
              print ('fiz')
              n=n+1
          elif n%5==0 and n%3 !=0:
              print ('buzz')  
              n=n+1
          elif n%3==0 and n!=0:
              print ('fizz, buzz')
              n=n+1
          else:
              print(n)
              n=n+1    
           


  


    
     
    