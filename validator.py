import re

COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "123456789", 
    "12345", "1234", "111111", "1234567", "dragon", "admin123"
}

def check_password_strength(password: str) -> dict:
    errors = []
    score = 0

    if not password:
        return {
            "score": 0,
            "status": "Invalid",
            "is_valid": False,
            "errors": ["Password can't be empty"]
        }
    if password in COMMON_PASSWORDS:
        return {
            "score": 0,
            "status": "Compromised",
            "is_valid": False,
            "ERRORS": ["Password is on Compromised LIST"]
        }
    if len(password) >= 8:
        score += 1
    else:
        errors.append("Password need to have atleast 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        errors.append("There is no Big Letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        errors.append("There is no SMall Letter")

    if re.search(r"\d", password):
        score += 1
    else:
        error.append("There is no digit")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        errors.append("Brak znaku specjalnego.")

    status_map = { 
        5: "STRONG",
        4: "MEDIUM",
        3: "WEAK"
    }
    status = status_map.get(score, "Very Weak")

    return { 
        "score": score,
        "status": status,
        "is_valid": len(errors) == 0,
        "errors": errors
    }