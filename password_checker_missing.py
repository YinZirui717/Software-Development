def check_password_strength(password):
    if not password:
        return "Password cannot be empty!"

    return "Password format accepted (no further checks in this version)."

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print(check_password_strength(pwd))
