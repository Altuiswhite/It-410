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

# Step 2: Create a total_hourly_rate list with 30% added
total_hourly_rate = [round(salary * 1.3, 2) for salary in hourly_salaries]

# Step 3: Check if maximum salary is over 37.30
max_salary = max(total_hourly_rate)
if max_salary > 37.30:
    print("⚠️ Warning: Someone's salary may be a budget concern!")

# Step 4: Find salaries between 28.15 and 30.65
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
# Check if we have more than 5 employees, more than 3 underpaid salaries,
# someone earns over $35/hr with benefits, and 'David Toma' is an employee.
if len(employee_numbers) > 5 and len(underpaid_salaries) > 3 and max_salary > 35 and "David Toma" in employee_names:
    print("⚠️ Complex Condition Met: Reevaluate pay structure and employee budget allocation.")

# Final output (optional display)
print("\nEmployee Numbers:", employee_numbers)
print("Employee Names:", employee_names)
print("Hourly Salaries:", hourly_salaries)
print("Total Hourly Rate (with benefits):", total_hourly_rate)
print("Underpaid Salaries:", underpaid_salaries)
print("Company Raises:", company_raises)
