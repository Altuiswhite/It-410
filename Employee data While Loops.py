# Initial raw data list
raw_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# Step 1: Separate into unique lists
employee_numbers = []
employee_names = []
hourly_salaries = []

for item in raw_data:
    if isinstance(item, int) and item > 1000:
        if item not in employee_numbers:
            employee_numbers.append(item)
    elif isinstance(item, str):
        if item not in employee_names:
            employee_names.append(item)
    elif isinstance(item, float):
        if item not in hourly_salaries:
            hourly_salaries.append(item)

# Step 2: Calculate total hourly rate with benefits (30% added)
total_hourly_rate = [round(salary * 1.3, 2) for salary in hourly_salaries]

# Step 3: Calculate company raises based on salary range
company_raises = []
for salary in hourly_salaries:
    if 22 <= salary < 24:
        raise_amount = round(salary * 1.05, 2)
    elif 24 <= salary < 26:
        raise_amount = round(salary * 1.04, 2)
    elif 26 <= salary < 28:
        raise_amount = round(salary * 1.03, 2)
    else:
        raise_amount = round(salary * 1.02, 2)
    company_raises.append(raise_amount)

# Step 4: Create database-like list of employee dictionaries
employees = []

# Ensure all lists have same length
min_length = min(len(employee_numbers), len(employee_names), len(hourly_salaries))

for i in range(min_length):
    employee = {
        "Employee ID": employee_numbers[i],
        "Name": employee_names[i],
        "Base Salary": hourly_salaries[i],
        "Hourly Rate with Benefits": total_hourly_rate[i],
        "Company Raise": company_raises[i]
    }
    employees.append(employee)

# Step 5: Display the employee database
print("\n📋 Final Employee Database (List of Dictionaries):")
for emp in employees:
    print(emp)
