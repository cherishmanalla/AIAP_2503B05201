from typing import List, Tuple


def sum_of_odd_numbers(numbers: List[int]) -> int:
    """Calculate the sum of all odd numbers in a list.

    Args:
        numbers: A list of integers.

    Returns:
        The sum of all odd numbers in the list.

    Examples:
        >>> sum_of_odd_numbers([1, 2, 3, 4, 5])
        9
        >>> sum_of_odd_numbers([2, 4, 6])
        0
    """
    return sum(n for n in numbers if n % 2 != 0)


def sum_of_even_numbers(numbers: List[int]) -> int:
    """Calculate the sum of all even numbers in a list.

    Args:
        numbers: A list of integers.

    Returns:
        The sum of all even numbers in the list.

    Examples:
        >>> sum_of_even_numbers([1, 2, 3, 4, 5])
        6
        >>> sum_of_even_numbers([1, 3, 5])
        0
    """
    return sum(n for n in numbers if n % 2 == 0)


def sum_odd_and_even(numbers: List[int]) -> Tuple[int, int]:
    """Calculate both sum of odd and even numbers in a single pass.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple (sum_of_odd, sum_of_even).

    Examples:
        >>> sum_odd_and_even([1, 2, 3, 4, 5])
        (9, 6)
    """
    odd_sum = 0
    even_sum = 0
    for n in numbers:
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return odd_sum, even_sum


if __name__ == '__main__':
    # Demo examples
    test_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [1, 3, 5, 7],
        [-1, -2, 3, 4],
        [],
    ]

    for nums in test_lists:
        odd_sum = sum_of_odd_numbers(nums)
        even_sum = sum_of_even_numbers(nums)
        combined_odd, combined_even = sum_odd_and_even(nums)
        
        print(f"\nList: {nums}")
        print(f"  Sum of odd numbers: {odd_sum}")
        print(f"  Sum of even numbers: {even_sum}")
        print(f"  Combined result: odd={combined_odd}, even={combined_even}")
