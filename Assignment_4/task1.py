def is_leap_year(year):
    """
    Check whether a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4 AND
    - If it is divisible by 100, it must also be divisible by 400
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def cm_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Args:
        centimeters (float): The length in centimeters
    
    Returns:
        float: The length in inches (rounded to 2 decimal places)
    """
    inches = centimeters / 2.54
    return round(inches, 2)


# Test cases
if __name__ == "__main__":
    test_years = [2000, 1900, 2004, 2023, 2024, 1996, 2100]
    
    print("Leap Year Tests:")
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year}: {'Leap year' if result else 'Not a leap year'}")
    
    print("\nCentimeters to Inches Conversion:")
    test_cm = [10, 25.4, 50, 100, 154]
    for cm in test_cm:
        inches = cm_to_inches(cm)
        print(f"{cm} cm = {inches} inches")
