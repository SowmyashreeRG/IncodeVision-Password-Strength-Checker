import re
import getpass


def check_password_strength(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character (e.g., !, @, #).")

    # Classify password strength
    if len(password) < 8 or score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, suggestions, score


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = getpass.getpass("Enter your password: ")

    if not password:
        print("\nError: Password cannot be empty.")
        return

    strength, suggestions, score = check_password_strength(password)

    print("\n--- PASSWORD ANALYSIS ---")
    print(f"Password length: {len(password)} characters")
    print(f"Criteria satisfied: {score}/5")
    print(f"Password strength: {strength}")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\nExcellent! Your password meets all five basic checks.")

    print("\nNote: This is a basic educational checker, not a guarantee")
    print("that a password is secure against real-world attacks.")
    print("=" * 45)


if __name__ == "__main__":
    main()