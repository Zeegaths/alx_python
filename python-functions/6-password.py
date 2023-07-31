def validate_password(password):
    # Check password length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digit in the password
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

        # Check for spaces in the password
        if char.isspace():
            return False

    # Check if all conditions are satisfied
    return has_uppercase and has_lowercase and has_digit
