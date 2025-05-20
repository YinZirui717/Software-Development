from checker.password_checker import check_password_strength

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(check_password_strength(password))
