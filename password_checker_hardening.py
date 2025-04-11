def check_password_strength(password):
    score = 0
    length = len(password)

    if length >= 16:
        score += 30
    elif length >= 12:
        score += 20
    elif length >= 8:
        score += 10
    else:
        return "Weak (password is too short)"

    if score < 40:
        return "Weak"
    elif score < 70:
        return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print(check_password_strength(pwd))
