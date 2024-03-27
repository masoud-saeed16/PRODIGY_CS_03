import re

def is_password_valid(password):
    """Check if the password meets the required criteria."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    elif not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    elif not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    elif not re.search("[0-9]", password):
        return False, "Password must contain at least one number"
    else:
        return True, "Password is Strong"

def main():
    """Main function to get user input and validate password."""
    password = input("Enter your Password: ")
    is_valid, message = is_password_valid(password)
    if is_valid:
        print(message)
    else:
        print("Invalid Password:", message)

if __name__ == "__main__":
    main()
