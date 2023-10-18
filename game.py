def my_choice():
 num = int(input("enter number"))      
 if num%3 == 0 :
      if num%5 == 0:
         print("fizz buzz")
         
      else:
       print("fizz")  
     
 elif num%5 == 0: 
      print('buzz')
 else:
       print("invalid input")
while(True):
      my_choice()
      choice=int(input("Do you want to play Press 0 to skip"))
      if choice == 0:
       break     
      