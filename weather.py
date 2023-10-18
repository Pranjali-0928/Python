weather = "raining"
my_preference = "hot"
if weather == "hot":
    if my_preference == "hot":
     print("i am having juice")
    else:
        print("i am having tea ")
elif weather == "raining":
    if my_preference == "hot":
       print("i am having tea")
    else:
        print("i am having cold cofee")
elif weather == "cold":
    if my_preference == "hot":
        print("i am having hottea")
    else:
     print("i am having coffe")
else:
    print("bye")
    