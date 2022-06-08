from string import ascii_lowercase, ascii_uppercase, digits

def password_validator(password):

    allowed_lenght = 8
    password_set = set(password)
    lowercase_set = set(ascii_lowercase)
    uppercase_set = set(ascii_uppercase)
    digits_set = set(digits)

    if len(password) >= allowed_lenght and password_set & lowercase_set \
        and password_set & uppercase_set and password_set & digits_set:
        
        return True
    else:
        return False