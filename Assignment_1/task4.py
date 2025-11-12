def factorial_recursive(n: int) -> int:
    """
    Recursive factorial:
    - Validates input is an int and non-negative.
    - Base case: 0! = 1 and 1! = 1.
    - Recursive case: n! = n * (n-1)!.
    """
    if not isinstance(n, int):
        raise TypeError("factorial_recursive() requires an integer")
    if n < 0:
        raise ValueError("factorial_recursive() requires a non-negative integer")
    # Base case
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Iterative factorial:
    - Validates input is an int and non-negative.
    - Uses a loop to multiply values from 2..n.
    """
    if not isinstance(n, int):
        raise TypeError("factorial_iterative() requires an integer")
    if n < 0:
        raise ValueError("factorial_iterative() requires a non-negative integer")
    result = 1
    # Multiply successive integers up to n
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    try:
        s = input("Enter a non-negative integer: ")
        n = int(s.strip())
    except (EOFError, KeyboardInterrupt):
        print()
        raise SystemExit(0)
    except ValueError:
        print("Invalid integer")
        raise SystemExit(1)

    print(f"{n}! (recursive) = {factorial_recursive(n)}")
    print(f"{n}! (iterative) = {factorial_iterative(n)}")