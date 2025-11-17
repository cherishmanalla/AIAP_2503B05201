def count_lines_in_file(filename):
    """
    Read a .txt file and return the number of lines.
    
    This function demonstrates AI-guided logic for file processing:
    - Opens the file safely using context manager (with statement)
    - Reads all lines from the file
    - Returns the total count of lines
    - Handles file not found errors gracefully
    
    Args:
        filename (str): The path to the .txt file to process
    
    Returns:
        int: The number of lines in the file, or -1 if file not found
    
    Examples:
        >>> count_lines_in_file("sample.txt")
        42
        
        >>> count_lines_in_file("nonexistent.txt")
        -1
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    except Exception as e:
        print(f"Error reading file: {e}")
        return -1


# Test cases and demonstration
if __name__ == "__main__":
    # Create sample test files for demonstration
    import os
    
    # Create test file 1
    test_file_1 = "test_sample_1.txt"
    with open(test_file_1, 'w') as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")
    
    # Create test file 2
    test_file_2 = "test_sample_2.txt"
    with open(test_file_2, 'w') as f:
        f.write("Hello World\n")
        f.write("Python is fun\n")
        f.write("File processing\n")
        f.write("Line 4\n")
        f.write("Line 5\n")
    
    # Create empty test file
    test_file_3 = "test_sample_empty.txt"
    with open(test_file_3, 'w') as f:
        pass  # Empty file
    
    # Run tests
    print("File Line Counting Test:")
    print("-" * 50)
    
    print(f"Counting lines in '{test_file_1}': {count_lines_in_file(test_file_1)} lines")
    print(f"Counting lines in '{test_file_2}': {count_lines_in_file(test_file_2)} lines")
    print(f"Counting lines in '{test_file_3}': {count_lines_in_file(test_file_3)} lines")
    print(f"Counting lines in 'nonexistent.txt': {count_lines_in_file('nonexistent.txt')} (file not found)")
    
    # Clean up test files
    print("-" * 50)
    print("Cleaning up test files...")
    os.remove(test_file_1)
    os.remove(test_file_2)
    os.remove(test_file_3)
    print("Test files removed.")
