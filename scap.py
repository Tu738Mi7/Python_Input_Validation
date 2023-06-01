import re


def sanitize_input(name):
    # Remove HTML tags using regular expression substitution
    sanitized_string = re.sub('<.*?>', '', name)
    # Remove special characters using regular expression substitution
    sanitized_string = re.sub('[^a-zA-Z0-9\s]', '', sanitized_string)
    return sanitized_string.strip()  # Strip leading and trailing whitespaces


def validate_input(name):
    # Check input for any malicious characters
    if re.search('[<>&\'"]', name):
        raise ValueError("Invalid input. Avoid using special characters.")


# Demo
user_input = input("Enter your name: ")

try:
    sanitized_input = sanitize_input(user_input)
    validate_input(sanitized_input)
    # Use the sanitized input in your application
    print("Sanitized input:", sanitized_input)
except ValueError as e:
    print("Error:", str(e))
