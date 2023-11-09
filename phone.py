import re

def is_mobile_number(phone_number):
    # Regular expression pattern for U.S. mobile numbers
    mobile_pattern = r'^\d{10}$'  # Assumes 10 digits without any formatting characters

    return bool(re.match(mobile_pattern, phone_number))

def is_landline_number(phone_number):
    # Regular expression pattern for U.S. landline numbers
    landline_pattern = r'^\d{3}-\d{3}-\d{4}$'  # Assumes the format (XXX-XXX-XXXX)

    return bool(re.match(landline_pattern, phone_number))

def check_phone_type(phone_number):
    if is_mobile_number(phone_number):
        return "Mobile"
    elif is_landline_number(phone_number):
        return "Landline"
    else:
        return "Unknown"

# Example usage:
phone_number = "555-555-5555"
phone_type = check_phone_type(phone_number)
print(f"{phone_number} is a {phone_type} number.")
  


#this logic cannot be implemented as the us landline number and phone number have the same format
# Landline phone numbers in the United States are typically represented in the format (XXX) XXX-XXXX, where X represents a digit.
#  Here's the pattern:

# Area Code (3 digits): Enclosed in parentheses (e.g., (123))
# Central Office Code (3 digits): Follows the area code (e.g., 456)
# Line Number (4 digits): Follows a hyphen (e.g., 7890)  
