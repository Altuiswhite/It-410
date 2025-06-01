# Program: Employee Information Collector
# Purpose: Use functions and while loops to collect, validate, and display employee information

# Function to get a valid employee ID (must be an integer > 1000)
def get_employee_id():
    while True:
        try:
            emp_id = int(input("Enter employee ID (numbers only): "))
            if emp_id > 1000:
                return emp_id
            else:
                print("Employee ID must be greater than 1000.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get a valid employee name (non-empty string)
def get_employee_name():
    while True:
        name = input("Enter employee name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")

# Function to get a valid hourly salary (must be a float > 0)
def get_hourly_salary():
    while True:
        try:
            salary = float(input("Enter hourly salary (e.g., 25.50): "))
            if salary > 0:
                return salary
            else:
                print("Salary must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to collect all data for one employee
def collect_employee_data():
    employee = {}
    employee["Employee ID"] = get_employee_id()
    employee["Name"] = get_employee_name()
    employee["Hourly Salary"] = get_hourly_salary()
    return employee

# Function to display a list of employee dictionaries
def display_employees(employee_list):
    print("\n📋 Final Employee List:")
    for emp in employee_list:
        print(f"ID: {emp['Employee ID']}, Name: {emp['Name']}, Salary: ${emp['Hourly Salary']:.2f}")

# Main logic: collect up to 5 employees, loop with option to stop early
def main():
    employees = []
    print("Welcome to the Employee Information Collector!\n")

    while len(employees) < 5:
        print(f"\nCollecting data for employee #{len(employees) + 1}")
        employee = collect_employee_data()
        employees.append(employee)

        if len(employees) < 5:
            choice = input("Would you like to add another employee? (y/n): ").strip().lower()
            if choice != 'y':
                break

    # Display final data
    display_employees(employees)

# Run the program
if __name__ == "__main__":
    main()
