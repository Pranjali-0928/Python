# try:
#      input_var = int(input("Please enter a number "))
# except Exception:
#     try:
#          input_var = int(input("Please enter a correct number "))
#     except:
#         input_var = int(input("you stupid,Please enter a correct number "))
# print("Adding 10 to your value entered is " , input_var+ 10)


# input_var = int(input("Please enter a number "))
# print("I came at this line ")

# if isinstance(input_var,int):
#     print("Adding 10 to your value entered is " , input_var+ 10)
# else:
#     input_var = int(input("You entered an incorrect number , Please try again ! "))
#     if isinstance(input_var,int):
#         print("Adding 10 to your value entered is " , input_var+ 10)
#     else:    
#         input_var = int(input("You stupid please enter a number"))    
#         if isinstance(input_var,int):
#             print("Adding 10 to your value entered is " , input_var+ 10)


# # with exceptions code  for a function to demonstrate exception propogation 
# def my_simple_fun():
#         return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"
        
# try:
#     print(my_simple_fun())
# except Exception:
#     try:
#         print(my_simple_fun())
#     except :
#         print(my_simple_fun())


# # with exceptions code  for a function but with other exception to demonstrate exception matching
# def my_simple_fun():
#         return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"
        
# try:
#     print(my_simple_fun())
# except Exception:
#     try:
#         print(my_simple_fun())
#     except :
#         print(my_simple_fun())



 # a function within a function to demonstrate exception propogation
def inner_simple_func():
    return f"Adding 10 to your value entered is  {int(input('Please enter a number '))+ 10}"

def my_simple_fun():
        print("Doing Nothing here -- just try to handle exception if possible ")
        return inner_simple_func()
        
try:
    print(my_simple_fun())
except Exception:
    try:
        print(my_simple_fun())
    except :
        print(my_simple_fun())