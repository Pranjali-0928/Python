def list_display_members(members) :
     print(len(members))
def list_add_element(members) :
	#pass # write your logic
    #members = input('for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania \n').split(",")
    add=input("enter the element you want to add")
    members.append(add)
    print(members)
def list_add_elements(members):
	#pass # write your logic
    #members = input('for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania \n').split(",")
    members += input("enter values to add separated by comma \n").split(",")
    print(members)

def list_remove_element(members) :
	#pass # write your logic
     remove=input("which element you want to remove")
     members.remove(remove)
     print(members)

def remove_last_element(members) :
	#pass # write your logic
     members.pop()
     print(members)
def display_3_4_5_element(members):
	#pass # write your logic
    print(members[3:6])
