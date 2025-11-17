"""
Task 3 – Recursive Fibonacci with Documentation
-----------------------------------------------

Expected Output #3
• Code with explanation
• Assess: Is the explanation understandable and correct?
"""

from functools import lru_cache


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)  for n >= 2

    Args:
        n: Zero-based position within the Fibonacci sequence. Must be >= 0.

    Returns:
        The integer Fibonacci value at index n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    @lru_cache(maxsize=None)
    def recurse(k: int) -> int:
        """Inner helper that performs the actual recursive computation with memoization."""
        if k < 2:
            return k
        return recurse(k - 1) + recurse(k - 2)

    return recurse(n)


CODE_EXPLANATION = """
The `fibonacci` function calculates the nth Fibonacci number by expressing the
problem recursively. After validating that `n` is non-negative, it defines a
memoized helper `recurse` so repeated subproblems are cached, preventing the
exponential blowup seen in naive recursion. The helper directly returns `k` when
`k` is 0 or 1, matching the base conditions of the Fibonacci definition, and
otherwise sums the two preceding Fibonacci numbers. Finally, `fibonacci` calls
`recurse(n)` and returns the resulting integer.
""".strip()


EXPLANATION_ASSESSMENT = "The explanation is understandable and accurately reflects how the code works."


if __name__ == "__main__":
    index = 10
    print(f"Fibonacci number at index {index}: {fibonacci(index)}")
    print("\nExplanation:")
    print(CODE_EXPLANATION)
    print("\nAssessment:")
    print(EXPLANATION_ASSESSMENT)

