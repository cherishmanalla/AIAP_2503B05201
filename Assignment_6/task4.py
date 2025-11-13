def sum_to_n(n: int) -> int:
    """
    Calculate the sum of the first n natural numbers using a for-loop.

    For example, sum_to_n(5) returns 15 (1 + 2 + 3 + 4 + 5).
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative.")

    total = 0
    for number in range(1, n + 1):
        total += number
    return total


def sum_to_n_while(n: int) -> int:
    """Alternative implementation using a while-loop."""
    if n < 0:
        raise ValueError("n must be non-negative.")

    total = 0
    current = 1
    while current <= n:
        total += current
        current += 1
    return total


if __name__ == "__main__":
    value = 10
    print(f"Sum of first {value} numbers (for-loop): {sum_to_n(value)}")
    print(f"Sum of first {value} numbers (while-loop): {sum_to_n_while(value)}")

