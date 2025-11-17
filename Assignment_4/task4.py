def count_vowels(string):
    """
    Count the number of vowels in a string.
    
    Args:
        string (str): The string to count vowels in
    
    Returns:
        int: The number of vowels (case-insensitive)
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


# Test cases
if __name__ == "__main__":
    test_strings = [
        "Hello World",
        "Python Programming",
        "AEIOU",
        "bcdfg",
        "The quick brown fox jumps over the lazy dog",
        "aEiOu"
    ]
    
    print("Vowel Counting:")
    for string in test_strings:
        vowel_count = count_vowels(string)
        print(f'"{string}" → {vowel_count} vowels')
