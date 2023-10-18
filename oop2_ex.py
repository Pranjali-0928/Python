# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects


class Emplyoee:
    department_name="HPCSA"
    def __init__(self,emid,emp_salary_,mgr_id):
        self.emailid=emid
        self.employeesalary=emp_salary_
        self.managerid=mgr_id
        print(f"employee id is {emid}\n employee salary is {emp_salary_}\n manager id is {mgr_id}")
    
     





def main():
    employee=Emplyoee(100,1000,1)
    print(employee.emailid)
    print(employee.employeesalary)
    print(employee.managerid)
    # del employee.emailid
    # print(employee.emailid)
    del employee
    print(employee.managerid)
if __name__ == "__main__":
    main()


