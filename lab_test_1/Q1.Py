"""
Q1.Py

Fibonacci implementations and prompt-refinement records for Cursor AI.

This file provides:
- `fibonacci_sequence(n)` -> list of first n Fibonacci numbers (n >= 1)
- `fibonacci(n)` -> nth Fibonacci number (1-indexed)
- input validation that accepts only positive integers (n >= 1)
- PROMPT_REFINEMENTS: list documenting prompt versions and outcomes

When run as a script this file runs a small demo and shows handling of
valid and invalid inputs.
"""

from typing import List


def _validate_positive_integer(n) -> int:
	"""Validate that n is a positive integer (>=1).

	Returns the integer value on success, raises ValueError on failure.
	"""
	# Accept int-like values but reject floats, negatives, zero, and non-numeric
	if isinstance(n, bool):
		# bool is subclass of int in Python; reject it explicitly
		raise ValueError("n must be a positive integer (bool is not allowed)")
	if not isinstance(n, int):
		raise ValueError("n must be a positive integer (type int required)")
	if n < 1:
		raise ValueError("n must be a positive integer (>= 1)")
	return n


def fibonacci_sequence(n: int) -> List[int]:
	"""Return the first n Fibonacci numbers as a list.

	The sequence is 1, 1, 2, 3, 5, ... (1-indexed). Only accepts positive
	integers for n (n >= 1).
	"""
	n = _validate_positive_integer(n)
	if n == 1:
		return [1]
	seq = [1, 1]
	while len(seq) < n:
		seq.append(seq[-1] + seq[-2])
	return seq


def fibonacci(n: int) -> int:
	"""Return the nth Fibonacci number (1-indexed).

	Uses an iterative approach (O(n) time, O(1) extra space).
	"""
	n = _validate_positive_integer(n)
	if n <= 2:
		return 1
	a, b = 1, 1
	for _ in range(3, n + 1):
		a, b = b, a + b
	return b


# Simple record of prompt refinements and outcomes for Cursor AI usage.
# This is a human-readable log embedded alongside the code so reviewers can
# see the prompt evolution and the reasoning behind input validation.
PROMPT_REFINEMENTS = [
	{
		"version": 1,
		"prompt": "Write Python code that prints the Fibonacci sequence.",
		"changes": "Initial broad prompt. Generated basic sequence but no input validation.",
		"outcome": "Code printed a fixed sequence or used n without checking types/values.",
	},
	{
		"version": 2,
		"prompt": (
			"Refine: Accept user input n and return first n Fibonacci numbers. "
			"Add input validation to ensure n is an integer."
		),
		"changes": "Added integer type checking but accepted 0 and negative integers.",
		"outcome": "Handled non-int types poorly (floats and strings either crashed or behaved unexpectedly).",
	},
	{
		"version": 3,
		"prompt": (
			"Refine: Accept only positive integers (n >= 1). Reject floats, zero, negative and boolean values. "
			"Return helpful ValueError messages describing allowed input."
		),
		"changes": "Tightened validation: check isinstance int, reject bool, ensure n >= 1, and raise ValueError with clear messages.",
		"outcome": (
			"Final implementation validates inputs robustly. Demo shows accepted inputs produce sequence and invalid inputs raise ValueError with explicit messages."
		),
	},
]


def _demo():
	"""Run a short demo showing correct and incorrect uses.

	This function prints outputs for several sample inputs and catches errors
	to show the validation messages.
	"""
	samples = [1, 2, 7, -1, 0, 2.5, True, "a"]
	print("PROMPT_REFINEMENTS (summary):")
	for p in PROMPT_REFINEMENTS:
		print(f"- v{p['version']}: {p['changes']}")
	print("\nDemo outputs:")
	for s in samples:
		try:
			seq = fibonacci_sequence(s)
			nth = fibonacci(s)
			print(f"n={s!r}: sequence({len(seq)}): {seq} -> nth={nth}")
		except Exception as e:
			print(f"n={s!r}: Error -> {e}")


if __name__ == "__main__":
	_demo()

