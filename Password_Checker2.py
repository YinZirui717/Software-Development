import re

def check_password_strength(password):

    if not password:
        return "Password cannot be empty!"

    score = 0

    length = len(password)
    if length >= 16:
        score += 30
    elif length >= 10:
        score += 20
    elif length >= 6:
        score += 10
    else:
        return "Weak (password id too short)"

    if re.search(r"\d", password): score += 20
    if re.search(r"[A-Z]", password): score += 10
    if re.search(r"[a-z]", password): score += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 10

    if score < 40:
        strength = "Weak"
    elif 40 <= score < 70:
        strength = "Moderate"
    else:
        strength = "Strong"

    return f"Password Strength: {strength} (Score: {score}/100)"

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(check_password_strength(password))