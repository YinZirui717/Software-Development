import re

def check_password_strength(password):

    # Re-uploaded using local merge strategy on 2025-04-11

    if not password:
        return "Password cannot be empty!"


    score = 0

    length = len(password)
    if length >= 12:
        score += 30
    elif length >= 8:
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

    missing = []

    for key, pattern in patterns.items():
        if not re.search(pattern, password):
                missing.append(key)
        else:
            score += 20

    score = min(score, 100)

    if score < 50:
        return f"Weak (Your password is missing: {', '.join(missing)})"
    elif 50 <= score < 90:
        strength = "Moderate"
    else:
        strength = "Strong"

    if missing:
        return f"Password Strength: {strength} (Score: {score}/100) — Missing: {', '.join(missing)}"
    else:
        return f"Password Strength: {strength} (Score: {score}/100)"

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(check_password_strength(password))