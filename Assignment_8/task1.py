import re


def is_valid_email(email):
    """
    Validates an email address based on the following rules:
    - Must contain @ and . characters
    - Must not start or end with special characters
    - Should not allow multiple @
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    # Check if email contains @ and . characters
    if '@' not in email or '.' not in email:
        return False
    
    # Check for multiple @ characters
    if email.count('@') != 1:
        return False
    
    # Define special characters (excluding @ and . which are allowed in the middle)
    # Common special characters that shouldn't be at start/end
    special_chars = r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,<>/?`~]'
    
    # Check if email starts or ends with special characters
    # We need to be careful - @ and . are special but have specific rules
    # Let's check for other special characters at start/end
    # Also check if it starts/ends with @ or .
    if email[0] in '@.' or email[-1] in '@.':
        return False
    
    # Check for other special characters at start/end (excluding @ and .)
    # Remove @ and . from the pattern for start/end check
    other_special = r'[!#$%^&*()_+\-=\[\]{};\':"\\|,<>/?`~]'
    if re.match(other_special, email[0]) or re.match(other_special, email[-1]):
        return False
    
    return True


# Test cases generated using AI reasoning
def test_is_valid_email():
    """Test suite for is_valid_email function"""
    
    # Valid email cases
    assert is_valid_email("user@example.com") == True, "Valid email should return True"
    assert is_valid_email("test.email@domain.co.uk") == True, "Email with subdomain should be valid"
    assert is_valid_email("name123@test.org") == True, "Email with numbers should be valid"
    assert is_valid_email("first.last@company.net") == True, "Email with dot in local part should be valid"
    assert is_valid_email("user_name@example-domain.com") == True, "Email with underscore and hyphen should be valid"
    assert is_valid_email("a@b.co") == True, "Short valid email should be valid"
    
    # Invalid: Missing @ character
    assert is_valid_email("userexample.com") == False, "Email without @ should return False"
    assert is_valid_email("user.example.com") == False, "Email without @ should return False"
    
    # Invalid: Missing . character
    assert is_valid_email("user@examplecom") == False, "Email without . should return False"
    assert is_valid_email("user@example") == False, "Email without . should return False"
    
    # Invalid: Multiple @ characters
    assert is_valid_email("user@@example.com") == False, "Email with multiple @ should return False"
    assert is_valid_email("user@example@domain.com") == False, "Email with multiple @ should return False"
    assert is_valid_email("@user@example.com") == False, "Email starting with @ should return False"
    
    # Invalid: Starting with special characters
    assert is_valid_email("@example.com") == False, "Email starting with @ should return False"
    assert is_valid_email(".user@example.com") == False, "Email starting with . should return False"
    assert is_valid_email("!user@example.com") == False, "Email starting with ! should return False"
    assert is_valid_email("#user@example.com") == False, "Email starting with # should return False"
    assert is_valid_email("$user@example.com") == False, "Email starting with $ should return False"
    assert is_valid_email("%user@example.com") == False, "Email starting with % should return False"
    
    # Invalid: Ending with special characters
    assert is_valid_email("user@example.com@") == False, "Email ending with @ should return False"
    assert is_valid_email("user@example.com.") == False, "Email ending with . should return False"
    assert is_valid_email("user@example.com!") == False, "Email ending with ! should return False"
    assert is_valid_email("user@example.com#") == False, "Email ending with # should return False"
    assert is_valid_email("user@example.com$") == False, "Email ending with $ should return False"
    
    # Invalid: Edge cases
    assert is_valid_email("") == False, "Empty string should return False"
    assert is_valid_email("@") == False, "Only @ should return False"
    assert is_valid_email(".") == False, "Only . should return False"
    assert is_valid_email("@.") == False, "Only @. should return False"
    assert is_valid_email("user@") == False, "Email ending with @ should return False"
    assert is_valid_email("@example.com") == False, "Email starting with @ should return False"
    assert is_valid_email("user.@example.com") == False, "Email with . before @ at start position should be checked"
    assert is_valid_email("user@.example.com") == False, "Email with . immediately after @ might be invalid but passes basic checks"
    
    # Invalid: None or non-string input
    assert is_valid_email(None) == False, "None should return False"
    
    print("All test cases passed! ✓")


if __name__ == "__main__":
    test_is_valid_email()
    print("\nEmail validation logic passing all test cases ✓")

