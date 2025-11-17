def format_name(first_name, last_name):
    """
    Format a full name as "Last, First".
    
    Args:
        first_name (str): The person's first name
        last_name (str): The person's last name
    
    Returns:
        str: The formatted name as "Last, First"
    """
    return f"{last_name}, {first_name}"


# Test cases
if __name__ == "__main__":
    test_names = [
        ("John", "Doe"),
        ("Jane", "Smith"),
        ("Alice", "Johnson"),
        ("Bob", "Williams"),
        ("Emma", "Brown")
    ]
    
    print("Name Formatting (Last, First):")
    for first, last in test_names:
        formatted = format_name(first, last)
        print(f"{first} {last} → {formatted}")
