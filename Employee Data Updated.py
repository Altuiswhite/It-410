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

# Step 1: Separate into unique lists for employee numbers, names, and hourly salaries
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

# Step 2: Create a total_hourly_rate list with 30% benefits added
total_hourly_rate = [round(salary * 1.3, 2) for salary in hourly_salaries]

# Step 3: Check for high salary warning
max_salary = max(total_hourly_rate)
if max_salary > 37.30:
    print("⚠️ Warning: Someone's salary may be a budget concern!")

# Step 4: Find underpaid salaries
underpaid_salaries = [rate for rate in total_hourly_rate if 28.15 <= rate <= 30.65]

# Step 5: Calculate company raises based on ranges
company_raises = []
for salary in hourly_salaries:
    if 22 <= salary < 24:
        new_salary = round(salary * 1.05, 2)
    elif 24 <= salary < 26:
        new_salary = round(salary * 1.04, 2)
    elif 26 <= salary < 28:
        new_salary = round(salary * 1.03, 2)
    else:
        new_salary = round(salary * 1.02, 2)
    company_raises.append(new_salary)

# Step 6: Complex condition with four truth tests
if len(employee_numbers) > 5 and len(underpaid_salaries) > 3 and max_salary > 35 and "David Toma" in employee_names:
    print("⚠️ Complex Condition Met: Reevaluate pay structure and employee budget allocation.")

# Step 7: Combine all data into a list of dictionaries (employee database)
employee_database = []

# Make sure lists are all equal in length before zipping
min_length = min(len(employee_numbers), len(employee_names), len(hourly_salaries), len(total_hourly_rate), len(company_raises))

for i in range(min_length):
    record = {
        "Employee ID": employee_numbers[i],
        "Name": employee_names[i],
        "Base Salary": hourly_salaries[i],
        "Total Hourly Rate (with benefits)": total_hourly_rate[i],
        "Raise Amount": round(company_raises[i] - hourly_salaries[i], 2)
    }
    employee_database.append(record)

# Step 8: Print final structured list
print("\n📋 Final Employee Database:")
for emp in employee_database:
    print(emp)
