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

    patterns = {
        "digits": r"\d",
        "uppercase": r"[A-Z]",
        "lowercase": r"[a-z]",
        "special_characters": r"[!@#$%^&*(),.?\":{}|<>]"
    }

    for key, pattern in patterns.items():
        if re.search(pattern, password):
            score += 20 

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