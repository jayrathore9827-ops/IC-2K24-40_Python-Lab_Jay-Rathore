employees = {}

def addEmployee():
    global employees
    emp_id = str(input("Enter Employee ID (e.g., E1): "))
    if emp_id in employees:
        print("Employee ID already exists!")
        return
    
    name = str(input("Enter Employee Name: "))
    dept = str(input("Enter Department: "))
    try:
        salary = float(input("Enter Salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid salary input. Please enter a number.")
        return
        
    employees[emp_id] = {"name": name, "dept": dept, "salary": salary}
    print("Employee added successfully!")

def updateSalary():
    global employees
    emp_id = str(input("Enter Employee ID to update: "))
    if emp_id not in employees:
        print("Employee not found!")
        return
    
    try:
        new_salary = float(input("Enter Updated Salary: "))
        if new_salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid salary input.")
        return
        
    employees[emp_id]["salary"] = new_salary
    print("Salary updated successfully!")

def deleteEmployee():
    global employees
    emp_id = str(input("Enter Employee ID to delete: "))
    deleted_record = employees.pop(emp_id, None)
    if deleted_record is not None:
        print(f"Employee {emp_id} ({deleted_record['name']}) deleted successfully.")
    else:
        print("Employee not found")

def searchEmployee():
    global employees
    emp_id = str(input("Enter Employee ID to search: "))
    if emp_id not in employees:
        print("Employee not found!")
        return
    
    emp = employees[emp_id]
    print(f"\n--- Employee Details ---")
    print(f"ID: {emp_id}")
    print(f"Name: {emp['name']}")
    print(f"Department: {emp['dept']}")
    print(f"Salary: {emp['salary']}")

def showReports():
    global employees
    if not employees:
        print("No employee records available.")
        return

    print("\n--- EMPLOYEE REPORTS ---")

    
    dept_stats = {}
    for emp_id, data in employees.items():
        dept = data['dept']
        salary = data['salary']
        
        
        dept_stats.setdefault(dept, {"payroll": 0.0, "headcount": 0})
        dept_stats[dept]["payroll"] += salary
        dept_stats[dept]["headcount"] += 1

    print("\n1. Department-wise Payroll and Headcount:")
    for dept, stats in dept_stats.items():
        print(f"   {dept} -> Total Payroll: {stats['payroll']}, Headcount: {stats['headcount']}")

    
    print("\n2. Highest-Paid Employee in Each Department:")
    dept_highest = {}
    for emp_id, data in employees.items():
        dept = data['dept']
        if dept not in dept_highest or data['salary'] > dept_highest[dept]['salary']:
            dept_highest[dept] = {"name": data['name'], "salary": data['salary']}
            
    for dept, info in dept_highest.items():
        print(f"   {dept} -> {info['name']} (Salary: {info['salary']})")

    
    print("\n3. Employees Sorted by Salary (Highest First):")
    sorted_employees = sorted(employees.items(), key=lambda item: item[1]['salary'], reverse=True)
    for emp_id, data in sorted_employees:
        print(f"   {emp_id}: {data['name']} ({data['dept']}) - Salary: {data['salary']}")

    updated_employees_raise = {
        emp_id: {**data, "salary": data["salary"] * 1.10} if data["salary"] < 50000 else data
        for emp_id, data in employees.items()
    }
    
    print("\n4. New Dictionary with 10% Raise for Salaries Below 50,000:")
    for emp_id, data in updated_employees_raise.items():
        print(f"   {emp_id}: {data['name']} -> New Salary: {data['salary']}")

    
    print("\n5. Department with the Highest Average Salary:")
    dept_averages = {
        dept: stats["payroll"] / stats["headcount"] 
        for dept, stats in dept_stats.items()
    }
    
    if dept_averages:
        highest_avg_dept = max(dept_averages, key=dept_averages.get)
        print(f"   {highest_avg_dept} with an average salary of {round(dept_averages[highest_avg_dept], 2)}")


while True:
    print("\n--- Employee Database Menu ---")
    print("1. Add an employee")
    print("2. Update employee salary")
    print("3. Delete an employee")
    print("4. Search employee by ID")
    print("5. Reports")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        addEmployee()
    elif choice == '2':
        updateSalary()
    elif choice == '3':
        deleteEmployee()
    elif choice == '4':
        searchEmployee()
    elif choice == '5':
        showReports()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")

