class Employee:
    #classs variable
    department_name="DevOPs"
    
    #initializer
    
    def __init__(self,emp_id,salary,mg_id):
        self.employee_id= emp_id
        self.salaary=salary
        self.manager=mg_id
        print(f"{self} was craeated successfully with values {emp_id}, {salary}, {mg_id}")
     #instant method   
    def get_emp_salary(self):
        return self.salaary
    def set_emp_salary(self,rcv_salary):
        self.salaary=rcv_salary
        
    @classmethod
    def deprtment(cls):
        return cls.department_name
    
    
    @staticmethod
    def field_expertise():
        print("experties  are 1)python ---- 2)c++ ---- 3)java\n")    
        
def main():
 emp1=Employee(1,1000000,10)
 emp2=Employee(2,1200000,11)
 emp1.field_expertise()
if __name__ == "__main__":
    main()