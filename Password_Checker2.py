import re

def check_password_strength(password):
    if not password:
        return "Password cannot be empty"

    score = 0
    if len(password) >= 6: score += 20
    if len(password) >= 10: score += 30
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
    print(check_password_strYZRyzr252618ength(password))