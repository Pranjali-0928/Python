def my_add():
   a = int(input("enter a number"))
   b = int(input("enter a number"))
   z=a+b
   print(z)
def my_sq():
   c = int(input("enter a number"))
   x=c**2
   print(x)
   
def my_expo():
   d = int(input("enter a number"))
   e = int(input("enter a number"))
   f=d**e
   print(f)
def my_avg():
  d = int(input("enter a number"))
  e = int(input("enter a number"))
  f=  int(input("enter a number"))
  g=(d+e+f)/3
  print(g)

print("1. addition", "\n","2.Square","\n","3.exponention","\n","4.average", "\n", "5.quit")
ch =  int(input("enter your choice from disply\n"))   
if ch == 1:
    my_add()
elif ch == 2:
    my_sq()
elif ch == 3:
    my_expo()
elif ch ==4:
    my_avg()
else:
    print("you choosed to quit")