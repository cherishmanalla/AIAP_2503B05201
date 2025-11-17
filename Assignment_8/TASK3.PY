import re


def is_sentence_palindrome(sentence):
    """
    Returns True if the sentence reads the same forwards and backwards
    when ignoring case, spaces, and punctuation. Otherwise returns False.
    """
    if not isinstance(sentence, str):
        return False

    # Keep only alphanumeric characters, lower-case them
    cleaned = re.sub(r"[^A-Za-z0-9]", "", sentence).lower()

    # Empty or 1-char strings are palindromes
    return cleaned == cleaned[::-1]


def test_is_sentence_palindrome():
    """AI-generated test cases covering positives, negatives, and edge cases."""

    # Classic palindromes (ignoring spaces/punctuation/case)
    assert is_sentence_palindrome("A man a plan a canal Panama") is True
    assert is_sentence_palindrome("Never odd or even") is True
    assert is_sentence_palindrome("Was it a car or a cat I saw?") is True
    assert is_sentence_palindrome("No 'x' in Nixon") is True
    assert is_sentence_palindrome("Madam In Eden, I'm Adam") is True
    assert is_sentence_palindrome("Able was I ere I saw Elba") is True
    assert is_sentence_palindrome("12321") is True
    assert is_sentence_palindrome("1 2 3 2 1") is True

    # Non-palindromes
    assert is_sentence_palindrome("Hello, World!") is False
    assert is_sentence_palindrome("Palindrome") is False
    assert is_sentence_palindrome("Python rocks") is False
    assert is_sentence_palindrome("12345") is False
    assert is_sentence_palindrome("This is not a palindrome") is False

    # Edge cases
    assert is_sentence_palindrome("") is True  # empty string
    assert is_sentence_palindrome(" ") is True  # single space
    assert is_sentence_palindrome("!!!") is True  # only punctuation -> empty string
    assert is_sentence_palindrome("A") is True  # single letter
    assert is_sentence_palindrome("aa") is True
    assert is_sentence_palindrome("ab") is False

    # Non-string inputs should return False
    assert is_sentence_palindrome(None) is False
    assert is_sentence_palindrome(12321) is False
    assert is_sentence_palindrome(["A", "man"]) is False

    print("All test cases for is_sentence_palindrome passed! ✓")


if __name__ == "__main__":
    test_is_sentence_palindrome()
    print("\nSentence palindrome logic passing all test cases ✓")

