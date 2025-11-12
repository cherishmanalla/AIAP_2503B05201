from typing import List, Union, Iterable


def sum_of_squares(numbers: Iterable[Union[int, float]]) -> Union[int, float]:
    """Calculate the sum of squares for a collection of numbers.

    Args:
        numbers: An iterable of numeric values (int or float).

    Returns:
        The sum of each number squared: sum(n^2 for n in numbers).

    Examples:
        >>> sum_of_squares([1, 2, 3])
        14
        >>> sum_of_squares([0])
        0
        >>> sum_of_squares([-1, 2, -3])
        14
    """
    return sum(n ** 2 for n in numbers)


if __name__ == '__main__':
    # Demo examples
    test_cases = [
        [1, 2, 3],
        [0],
        [-1, 2, -3],
        [5.5, 2.5],
        [],
    ]

    for nums in test_cases:
        result = sum_of_squares(nums)
        print(f"sum_of_squares({nums}) = {result}")
