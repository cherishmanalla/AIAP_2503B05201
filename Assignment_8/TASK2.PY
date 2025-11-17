def assign_grade(score):
    """Assigns a letter grade based on the score"""
    # Check if score is a valid number
    if not isinstance(score, (int, float)):
        return None
    
    # Check if score is within valid range (0-100)
    if score < 0 or score > 100:
        return None
    
    # Assign grade based on score ranges
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def test_assign_grade():
    """Test suite for assign_grade function"""
    
    # Grade A (90-100)
    assert assign_grade(100) == 'A'
    assert assign_grade(95) == 'A'
    assert assign_grade(90) == 'A'
    
    # Grade B (80-89)
    assert assign_grade(89) == 'B'
    assert assign_grade(85) == 'B'
    assert assign_grade(80) == 'B'
    
    # Grade C (70-79)
    assert assign_grade(79) == 'C'
    assert assign_grade(75) == 'C'
    assert assign_grade(70) == 'C'
    
    # Grade D (60-69)
    assert assign_grade(69) == 'D'
    assert assign_grade(65) == 'D'
    assert assign_grade(60) == 'D'
    
    # Grade F (<60)
    assert assign_grade(59) == 'F'
    assert assign_grade(50) == 'F'
    assert assign_grade(0) == 'F'
    
    # Invalid inputs - negative numbers
    assert assign_grade(-5) == None
    assert assign_grade(-1) == None
    
    # Invalid inputs - scores above 100
    assert assign_grade(105) == None
    assert assign_grade(101) == None
    
    # Invalid inputs - non-numeric strings
    assert assign_grade("eighty") == None
    assert assign_grade("90") == None
    assert assign_grade("abc") == None
    
    # Invalid inputs - other types
    assert assign_grade(None) == None
    
    print("All test cases passed! ✓")


if __name__ == "__main__":
    test_assign_grade()
    print("\nGrade assignment function passing test suite ✓")
    