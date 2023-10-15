 Exercise on Inheritance:
# -------------------------
# Create a base class named Employee as follows:
# Employee (
# -- class variables and methods
# 	organisation_name, 
# 	get_organisation_name(),
# 	set_organisation_name(org_name)

# -- instance variables and methods()
# emp_id,
# name,
# base_location,
# deployed_location,
# designation,
# salary ,
# get_employee_details() 	


# Create a subclass of Employee named Manager as follows:
# Manager(
	
# 	-- instance variables and methods()
# 	managed_employees[],
# 	perform_appraisal_for_an_employee(emp_id,percent_raise),
# 	get_manager_details(mgr_id)
# )

# Write a main method that does the following:
# create 3 objects of Employee 
# create an object of Manager_class and add the above 3 employee objects created as managed employees 
# display get_manager_details()
# for an employee do perform_appraisal_for_an_employee()

class Employee:
    organisation_name="cdac"
    def __init__(self,emp_id,name,base_location,deploy_location,designation,salary):
        self.empid=emp_id
        self.name1=name
        self.baselocation=base_location
        self.deploylocation=deploy_location
        self.designation1=designation
        self.salary1=salary
        print(f"employee id is {self.empid}\n name is {self.name1}\n base lacation is {self.baselocation}\n deploy locatio is {self.deploylocation}\n designation is {self.designation1}\n salary is {self.salary1} ")
    
    
    def get_employee_details(self):
        return (self.empid ,self.name1,self.baselocation,self.deploylocation,self.designation1,self.salary1 )
        
    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name  
    
    @classmethod
    def set_organisation_name(cls,org_name):
      cls.organisation_name=org_name
      
class Manager(Employee):
    def __init__(self,emp_id,name,base_location,deploy_location,designation,salary,list):
        super().__init__(emp_id,name,base_location,deploy_location,designation,salary)
        self.list1=list
        
        print(f"employee id is {self.empid}\n name is {self.name1}\n base lacation is {self.baselocation}\n deploy locatio is {self.deploylocation}\n designation is {self.designation1}\n salary is {self.salary1}\n ")
        for i in self.list1:
            print(i.get_employee_details())
    def perform_appraisal_for_an_employee(self,emp_obj,percantage_raise):
        current_salary=emp_obj.salary1
        increment=current_salary*percantage_raise/100
        emp_obj.salary1=int(increment)+int(current_salary)   
            
def main():
    
    emp1=Employee(1,'Sukanya','pune','Banglore','HPC_Administrator',1000000)
    emp2=Employee(2,'Pranjali','pune','Hydrabad','HPC_Administrator',1000000)
    emp3=Employee(3,'anonymous','Mumbai','chennai','Null',1000000)
    list=[emp1,emp2,emp3]
    man=Manager(4,'anonymouss','Mumbaii','chennaii','Nulll',1000000,list)
    man.perform_appraisal_for_an_employee(emp2,100)
    
    print(emp2.get_employee_details())
      
if __name__=="__main__": 
    main()  
