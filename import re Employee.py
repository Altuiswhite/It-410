import re
import sys

# Step 1: Define invalid characters for each field
invalid_name_chars = r'["!@#$%^&*()_=+<>/?;:\[\]{}\\]'
invalid_email_chars = r'["!\'#\$%\^&\*\(\)=+<>\?;:\[\]{}\\]'
invalid_address_chars = r'["!\'@$%^&*_=<>\?;:\[\]{}]'

# Step 2: Get Employee ID
employee_id = input("Enter Employee ID (up to 7 digits): ")

# Validate Employee ID: must be numeric and 7 digits or fewer
if not employee_id.isdigit() or len(employee_id) > 7:
    print("❌ Invalid Employee ID. Program will terminate.")
    sys.exit()

# Step 3: Get Employee Name
employee_name = input("Enter Employee Name: ")

# Validate name: must not contain invalid characters
if re.search(invalid_name_chars, employee_name):
    print("❌ Invalid Employee Name. Program will terminate.")
    sys.exit()

# Step 4: Get Email Address
employee_email = input("Enter Employee Email Address: ")

# Validate email: must not contain invalid characters
if re.search(invalid_email_chars, employee_email):
    print("❌ Invalid Email Address. Program will terminate.")
    sys.exit()

# Step 5: Get Address (optional)
employee_address = input("Enter Employee Address (optional): ")

# If address is provided, validate it
if employee_address.strip() != "":
    if re.search(invalid_address_chars, employee_address):
        print("❌ Invalid Address. Program will terminate.")
        sys.exit()
    address_provided = True
else:
    address_provided = False

# Step 6: Final message
print(f"\n✅ Hello, {employee_name}. Your Employee ID is {employee_id}, and your email address is {employee_email}.")
if address_provided:
    print(f"Your address is {employee_address}.")
else:
    print("You did not provide an address.")
