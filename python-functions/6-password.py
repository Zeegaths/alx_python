def validate_password(password):
    if len(password) < 8:
        return False
    if char.isspace():
            return False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        return True
    else: 
         return False
 
