class Student:
    """ This is doctstring for Student class """
    # class variable
    school_name = "CDAC"    
    
    # initialiser
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course):
        # instance variable
        self.__student_name = rcv_name      # private instance variable 
        self._student_rollno = rcv_rollno   # protected instance variable
        self.student_pocket_money = rcv_pocket_money # public instance variable 
        self.student_enrolled_coursename = rcv_course # public instance variable 
        
    def get_student_name(self):
        return self.__student_name  
    def set_student_name(self,rcv_name):  
        self.__student_name = rcv_name
    
    
    
    
    
    @classmethod
    def change_school_name(cls,abc):
        cls.school_name = abc
    
     # Operator Overloading -- implemented this to support greater than operation for Student class 
    def __gt__(self,pratik):
        return self._student_rollno > pratik._student_rollno    
    
    # # Operator Overloading -- implemented this to support Equal to operation for Student class 
    def __eq__(self,other_obj):
       return (self.__student_name == other_obj.__student_name  and 
               self._student_rollno == other_obj._student_rollno and
               self.student_pocket_money == other_obj.student_pocket_money and
               self.student_enrolled_coursename == other_obj.student_enrolled_coursename)

def main():
    print("I am in main and I am not part of the class ")

    # create a Student object referenced by gaurav
    # gaurav=pratik= Student("Gaurav",1,100,'Python')
    pranjali=pratik=gaurav= Student("Gaurav",1,100,'Scala')
    # Pranjali = Student("Pranjali",2,200,'Pythhon')
    # pratik= Student("Pratik",2,200,'Pythhon')
    # #set private variable
    # gaurav.__student_name = "" 
    # # print(gaurav.__student_name)
    # print(gaurav._Student__student_name)
    
    #set protected variable
    # print(gaurav._student_rollno)
    # gaurav._student_rollno = 3333333
    # print("After setting the protected variable : ", gaurav._student_rollno) 
    
    #set public variable
    # print(gaurav.student_enrolled_coursename)
    # gaurav.student_enrolled_coursename = 'linux'
    # print(gaurav.student_enrolled_coursename)

    #miscellnous functions for the class 
    # list all that the Student Class contains 
    # print(dir(Student))
    # # print(Student.__doc__)
    # gaurav.set_student_name("asd")
    # print(gaurav.get_student_name())
    
    
    # #gaurav.change_school_name("sunbeam") # this will change the class variable 
    # gaurav.school_name = "sunbeam" # this will create a new instance variable for gaurav instance 

    # # print the class variable 
    # print("School name at Class level is",Student.school_name)
    # print("Gaurav School name is",gaurav.school_name)
    # print("dug School name is",duplicate_gaurav.school_name)    
    # Student.change_school_name("Sunbeam")

    # print("School name at Class level was",Student.school_name)
    # print("Gaurav School name was",gaurav.school_name)
    # print("Pratik School name was",pratik.school_name)
    if gaurav==pratik==pranjali:
         print("equal")
    else:
         print("not equal")

      # operator > is overloaded 
    if gaurav>pratik:
         print("Greater")
    else:
         print("Lesser")
    
if __name__ == "__main__":
    main()
    