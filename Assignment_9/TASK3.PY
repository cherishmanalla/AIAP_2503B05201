"""Manual NumPy-style documentation for a basic calculator module.

This script demonstrates how to apply structured docstrings across multiple
functions while also capturing AI-generated alternatives for comparison.
"""

from typing import Tuple

# AI-generated docstrings recorded via Cursor AI suggestions.
AI_MODULE_DOCSTRING = """
Utility functions for simple arithmetic operations with explanatory docstrings.
"""

AI_FUNCTION_DOCSTRINGS = {
    "add": """
    Adds two numbers and returns their sum.
    """,
    "subtract": """
    Subtracts the second number from the first and returns the result.
    """,
    "multiply": """
    Multiplies two numbers and returns the product.
    """,
    "divide": """
    Divides the first number by the second and returns the quotient.
    Raises an error if the divisor is zero.
    """,
}


def add(x: float, y: float) -> float:
    """Add two numbers.

    Parameters
    ----------
    x : float
        First addend.
    y : float
        Second addend.

    Returns
    -------
    float
        Sum of ``x`` and ``y``.
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract ``y`` from ``x``.

    Parameters
    ----------
    x : float
        Minuend value.
    y : float
        Subtrahend value.

    Returns
    -------
    float
        Difference ``x - y``.
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply two numbers.

    Parameters
    ----------
    x : float
        First factor.
    y : float
        Second factor.

    Returns
    -------
    float
        Product of ``x`` and ``y``.
    """
    return x * y


def divide(x: float, y: float) -> float:
    """Divide ``x`` by ``y``.

    Parameters
    ----------
    x : float
        Dividend value.
    y : float
        Divisor value.

    Returns
    -------
    float
        Quotient ``x / y``.

    Raises
    ------
    ZeroDivisionError
        If ``y`` equals zero.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y


def summarize_docstrings() -> Tuple[str, dict]:
    """Return the manual and AI-generated docstrings for comparison."""
    manual_docs = {
        "module": __doc__,
        "add": add.__doc__,
        "subtract": subtract.__doc__,
        "multiply": multiply.__doc__,
        "divide": divide.__doc__,
    }
    ai_docs = {"module": AI_MODULE_DOCSTRING.strip(), **{k: v.strip() for k, v in AI_FUNCTION_DOCSTRINGS.items()}}
    return manual_docs, ai_docs


def main() -> None:
    """Execute sample operations and display docstring comparisons."""
    a, b = 12.0, 3.0
    print(f"Inputs: a={a}, b={b}")
    print(f"add -> {add(a, b)}")
    print(f"subtract -> {subtract(a, b)}")
    print(f"multiply -> {multiply(a, b)}")
    print(f"divide -> {divide(a, b)}")

    manual, ai = summarize_docstrings()
    print("\n--- Manual NumPy-style Docstrings ---")
    for key, text in manual.items():
        print(f"\n[{key.upper()}]\n{text.strip()}")

    print("\n--- AI-generated Docstrings ---")
    for key, text in ai.items():
        print(f"\n[{key.upper()}]\n{text}")

    print(
        "\nObservation: manual docstrings follow NumPy style with explicit sections, "
        "while AI versions are concise descriptions without structured headings. "
        "Both convey purpose, but NumPy style improves consistency and readability."
    )


if __name__ == "__main__":
    main()


