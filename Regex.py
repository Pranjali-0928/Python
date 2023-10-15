# Given the list of strings as input :

# gaurav1234@gmail.com
# pratik190900234@gmail.com
# 2009_rocking_person@yahoo.com
# GodFather2022@yahoo.com
# Brocklesner_89_WWE@yahoo.com
# TheRock_WWE@yahoo.com
# JohnCena_WWE@yahoo.com
# Undertaker_Roman_reigns@outlook.com
# 6789764666@rediffmail.com
# Kane#6789@gmail.com

# 1) provide me the list of emails that do have special characters of #~`!
# 2) provide me the list of emails that start with numbers
# 3) provide me the list of emails that start with numbers followed by an underscore
# 4) provide me the list of emails that start with numbers followed by an underscore or small case characters
# 5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
# 6) Provide me list of emails with only numbers before the @
# 7) Provide me list of emails with numbers anywhere before the @

# """
import re
a ="gaurav1234@gmail.com"
b="pratik190900234@gmail.com"
c="2009_rocking_person@yahoo.com"
d="GodFather2022@yahoo.com"
e="Brocklesner_89_WWE@yahoo.com"
f="999878WWE@yahoo.com"
g="JohnCena_WWE@yahoo.com"
h="Undertaker_Roman_reigns@outlook.com"
i="6789764666a@rediffmail.com"
j="Kane#6789@gmail.com"

#list1 =[a,b,c,d,e,f,g,h,i,j]
# for i in list1: 
#       result = re.search("[* #~`!]", i)  
#       if result :
#         print(f"{i}")



# list1 =[a,b,c,d,e,f,g,h,i,j]
# for i in list1: 
#       result = re.search("^[0-9]+", i)  
#       if result :
#         print(f"{i}")


# list1 =[a,b,c,d,e,f,g,h,i,j]
# for i in list1: 
#       result = re.search("^[\d]+_", i)  
#       if result :
#         print(f"{i}")


# list1 =[a,b,c,d,e,f,g,h,i,j]
# for i in list1: 
#       result = re.search("^[\d]+[_a-z]", i)  
#       if result :
#         print(f"{i}")


# list1 =[a,b,c,d,e,f,g,h,i,j]
# for i in list1: 
#       result = re.search("^[\d]+[_a-zA-Z]", i)  
#       if result :
#         print(f"{i}")


# list1 =[a,b,c,d,e,f,g,h,i,j]
# for i in list1: 
#       result = re.search("^[\d]+@", i)  
#       if result :
#         print(f"{i}")

list1 =[a,b,c,d,e,f,g,h,i,j]
for i in list1: 
      result = re.search(".*\d", i)  
      if result :
        print(f"{i}")
