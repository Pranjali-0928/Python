# """
# 3)  Create a program named "my_set_store" which support following operations on two sets
#     provided by user 

# for ex: 
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user

# Operations supported by our program are :
# 	1: Union
# 	2: Intersection 
# 	3: A-B
# 	4: B-A
# 	5: Take a element from user and Display if that element is a member of set B 
# 	6: Display number of elements in the set A
#     7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A
# """
# # Sample code template for my set store
def set_union(setA,setB) :
	print(setA.union(setB))
    

# write logic here 

def set_intersection(setA,setB) :
	print(setA.intersection(setB)) # write logic here 

def set_minus(setA,setB) :
	print(setA.difference(setB)) # write logic here 

def is_member_of_set(setB) :
    val1=input("enter a value to check")
    # setC=set()
    # setC.ad
    print(val1 in setB)
    
def set_display(setA):
	print(len(setA)) 
    
    
    
		
def set_add_element(setA):
	# pass # write logic here 
    add_elem=input("enter the element that you want add:")
    setA.add(add_elem)
    print(setA)

def set_add_elements(setA):
	# pass # write logic here
     add_elem2=input("enter multiple element you want add:")
     setA.update({add_elem2})
     print(setA)
     
def set_remove_element(setA):
	# pass # write logic here 
    elemdel=input("enter element which you to delet from setA:")
    setA.discard(elemdel)
    print(setA)

def my_set_store():
	print("\n Welcome to Our Set Store !!! ")

	setA= set(input("Please enter comma seperated elements for the set A").split(","))
	setB= set(input("Please enter comma seperated elements for the set B").split(","))
 
	while(True):
		print("\n*************** Menu **********************")
		print("Operations supported by our program are :")
		print("	1: Union")
		print("	2: Intersection ")
		print("	3: A-B")
		print("	4: B-A")
		print("	5: Take a element from user and Display if that element is a member of set B ")
		print("	6: Display number of elements in the set A")
		print(" 7: Display number of elements in the set B")
		print("	8: Add an element taken from the user to the set A")
		print("	9: Add multiple elements taken from the user to the set A")
		print("	10: Remove an element taken from the user from set A")
		print(" 11: Exit")

		choice = int(input("Please enter your choice "))

		if choice   ==1:
			set_union(setA,setB) 
		elif choice ==2:
			set_intersection(setA,setB)
		elif choice ==3:
			set_minus(setA,setB)
		elif choice ==4:
			set_minus(setB,setA)
		elif choice ==5:
			is_member_of_set(setB) 
		elif choice ==6:
			set_display(setA)
		elif choice ==7:
			set_display(setB)
		elif choice ==8:
			set_add_element(setA)
		elif choice ==9:
			set_add_elements(setA)
		elif choice ==10:
			set_remove_element(setA)
		elif choice ==11:
			break
		else:
			print("Invalid Input , Please Try Again !!!!  ")  
			
my_set_store()