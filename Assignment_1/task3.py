def reverse_string(s: str) -> str:
    """Return the reversed version of the input string."""
    if not isinstance(s, str):
        raise TypeError("reverse_string() requires a string")
    return s[::-1]

# Recursive factorial
def factorial_recursive(n: int) -> int:
    """
    Compute n! using recursion.
    - Raises TypeError if n is not an int.
    - Raises ValueError if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("factorial_recursive() requires an integer")
    if n < 0:
        raise ValueError("factorial_recursive() requires a non-negative integer")
    # Base case: 0! = 1 and 1! = 1
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial_recursive(n - 1)

# Iterative factorial
def factorial_iterative(n: int) -> int:
    """
    Compute n! using an iterative loop.
    - Raises TypeError if n is not an int.
    - Raises ValueError if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("factorial_iterative() requires an integer")
    if n < 0:
        raise ValueError("factorial_iterative() requires a non-negative integer")
    result = 1
    # Multiply 2..n into result
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        s = input("Enter a string: ")
    except (EOFError, KeyboardInterrupt):
        print()
        raise SystemExit(0)
    print(reverse_string(s))