from validator import check_password_strength

#Test - Empty STRING/PASSWORD

def test_empty_password():
    result = check_password_strength("")
    assert result["score"] == 0
    assert result["is_valid"] is False
    assert result["status"] == "Invalid"
    assert "Password can't be empty" in result["errors"]

#Test - Compromised passwords

def test_compromised_password():
    result = check_password_strength("123456")
    assert result["score"] == 0
    assert result["is_valid"] is False
    assert result["status"] == "Compromised"

#Test - Short password

def test_short_password():
    result = check_password_strength("Ab1!xyz")
    assert result["is_valid"] is False
    assert "Password need to have atleast 8 characters" in result["errors"]

#Test - Check for special characters

def test_missing_special_character():
    result = check_password_strength("MojeBezpieczne123")
    assert result["is_valid"] is False
    assert "Brak znaku specjalnego." in result["errors"]

#Test - For password Strength

def test_strong_valid_password():
    result = check_password_strength("TrudneHaslo123!")
    assert result["score"] == 5
    assert result["is_valid"] is True
    assert result["status"] == "STRONG"