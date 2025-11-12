from typing import Iterable


def is_palindrome(s: str,
                  *,
                  ignore_spaces: bool = True,
                  ignore_case: bool = True,
                  alphanumeric_only: bool = True) -> bool:
    """Return True if string `s` is a palindrome under the given rules.

    Parameters
    - s: input string
    - ignore_spaces: if True, spaces are ignored
    - ignore_case: if True, comparison is case-insensitive
    - alphanumeric_only: if True, only letters and digits are considered (punctuation ignored)

    Examples:
        is_palindrome('Racecar') -> True
        is_palindrome('A man, a plan, a canal: Panama') -> True
    """
    if s is None:
        return False

    def char_filter(ch: str) -> bool:
        if ch.isspace() and ignore_spaces:
            return False
        if alphanumeric_only:
            return ch.isalnum()
        return True

    # Build normalized character sequence
    if ignore_case:
        seq = [ch.lower() for ch in s if char_filter(ch)]
    else:
        seq = [ch for ch in s if char_filter(ch)]

    # Two-pointer check
    i, j = 0, len(seq) - 1
    while i < j:
        if seq[i] != seq[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    samples = [
        'racecar',
        'RaceCar',
        'A man, a plan, a canal: Panama',
        'No lemon, no melon',
        'not a palindrome',
    ]
    for s in samples:
        print(f"{s!r}: {is_palindrome(s)}")
