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
    test_cm = [10, 25.4, 50, 100, 154]
    
    print("Centimeters to Inches Conversion:")
    for cm in test_cm:
        inches = cm_to_inches(cm)
        print(f"{cm} cm = {inches} inches")
