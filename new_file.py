a = int(input("enter a number"))
b= int(input("enter a number"))
sum=a+b
print(sum)
sq=a*a
print(sq)
print(pow(a,b))
str = input("enter string:")
x = str.upper()
print (x)
 
height = int(input("enter the height in cm"))
inch=0.39370079*height
feet=0.0328084*height
print(int(inch))
print(int(feet))
dollar=int(input("enter dollar"))
rupees=82*dollar
print(rupees)
source=input("enter the source")
destination=input("enter the destination")
fare=int(input("enter fare in rupees"))
discount_rate=int(input("enter discount_rate percentage "))
print(f"fare from {source} to {destination} is { fare- (fare*discount_rate/100)} INR with has a discount of {discount_rate}%")