from typing import Sequence, Union

Number = Union[int, float]

def find_max(nums: Sequence[Number]) -> Number:
    """
    Return the largest number in a non-empty sequence (list/tuple).
    Raises TypeError if nums is not a list/tuple and ValueError if it's empty.
    Time: O(n), Space: O(1) extra.
    """
    if not isinstance(nums, (list, tuple)):
        raise TypeError("find_max() requires a list or tuple")
    if not nums:
        raise ValueError("find_max() requires a non-empty sequence")

    max_val = nums[0]
    for x in nums[1:]:
        if x > max_val:
            max_val = x
    return max_val


if __name__ == "__main__":
    # Prompt repeatedly until valid input or user quits
    while True:
        try:
            s = input("Enter numbers separated by spaces (or 'q' to quit): ").strip()
            if s.lower() in ("q", "quit", "exit"):
                raise SystemExit(0)
            if not s:
                print("No numbers provided. Try again.")
                continue
            nums = [float(tok) for tok in s.split()]
        except (EOFError, KeyboardInterrupt):
            print()
            raise SystemExit(0)
        except ValueError:
            print("Invalid number in input. Try again.")
            continue

        print("Largest number:", find_max(nums))
        break