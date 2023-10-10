# Initialize an empty dictionary
employee_info = {}

# Take input from the user for each key-value pair
employee_info['employee_id'] = int(input("Enter employee ID: "))
employee_info['employee_name'] = input("Enter employee name: ")
employee_info['account_number'] = int(input("Enter account number: "))
employee_info['salary'] = float(input("Enter salary: "))
employee_info['address'] = {
    'home_address': input("Enter home address: "),
    'work_address': input("Enter work address: ")
}
employee_info['awards'] = input("Enter awards (comma-separated): ").split(',')
employee_info['subjects_enrolled'] = tuple(input("Enter subjects enrolled (comma-separated): ").split(','))

# Print the resulting dictionary
print(employee_info)
