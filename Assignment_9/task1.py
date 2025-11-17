from collections.abc import Iterable
from typing import Tuple


def sum_even_and_odd(numbers: Iterable[int]) -> Tuple[int, int]:
    """Compute the sums of even and odd integers from the given iterable.

    This manual docstring explains the function in Google Style format.

    Args:
        numbers (Iterable[int]): The sequence of integers to inspect.

    Returns:
        Tuple[int, int]: A pair containing (even_sum, odd_sum).

    Raises:
        TypeError: If any element in ``numbers`` is not an integer.
    """
    even_sum = 0
    odd_sum = 0

    for value in numbers:
        if not isinstance(value, int):
            raise TypeError("All elements must be integers.")

        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return even_sum, odd_sum


# AI-generated docstring via Cursor AI suggestion for comparison.
AI_GENERATED_DOCSTRING = """
Summarizes even and odd totals from a list of integers.

Args:
    numbers: Collection of integers to analyze.

Returns:
    Tuple containing the cumulative even values followed by odd values.
"""


def _read_ints_from_input(user_input: str) -> list[int]:
    """Convert the raw string input into a list of integers."""
    if not user_input.strip():
        raise ValueError("Input cannot be empty.")

    return [int(part) for part in user_input.split()]


def main() -> None:
    """Entry point for collecting input and displaying the comparison."""
    try:
        raw_values = input("Enter integers separated by spaces: ")
        numbers = _read_ints_from_input(raw_values)
        even_sum, odd_sum = sum_even_and_odd(numbers)
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return
    except TypeError as exc:
        print(f"Type error: {exc}")
        return

    print(f"Even sum: {even_sum}")
    print(f"Odd sum: {odd_sum}")

    print("\nManual docstring for sum_even_and_odd:")
    print(sum_even_and_odd.__doc__)

    print("AI-generated docstring:")
    print(AI_GENERATED_DOCSTRING.strip())


if __name__ == "__main__":
    main()

