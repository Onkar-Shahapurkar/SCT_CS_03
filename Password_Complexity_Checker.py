import re


def assess_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Initialize strength score
    strength_score = 0

    # Evaluate each criterion
    if length_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if number_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1

    # Determine strength level
    if strength_score == 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong"
    elif strength_score == 3:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    # Return detailed results
    return {
        "password": password,
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "number_criteria": number_criteria,
        "special_char_criteria": special_char_criteria,
        "strength_score": strength_score,
        "strength_level": strength_level
    }


# Main function to get user input and display the result
if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    result = assess_password_strength(password)

    print(f"Password: {result['password']}")
    print(f"  Length >= 8: {result['length_criteria']}")
    print(f"  Contains uppercase: {result['uppercase_criteria']}")
    print(f"  Contains lowercase: {result['lowercase_criteria']}")
    print(f"  Contains number: {result['number_criteria']}")
    print(f"  Contains special char: {result['special_char_criteria']}")
    print(f"  Strength score: {result['strength_score']}")
    print(f"  Strength level: {result['strength_level']}")