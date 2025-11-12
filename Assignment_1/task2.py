def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, False otherwise.

    Uses simple checks for small n and 6k±1 optimization for trial division.
    """
    if not isinstance(n, int):
        raise TypeError("is_prime() requires an integer")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    try:
        s = input("Enter an integer: ")
        n = int(s.strip())
    except (EOFError, KeyboardInterrupt):
        print()
        raise SystemExit(0)
    except ValueError:
        print("Invalid integer")
        raise SystemExit(1)

    if is_prime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")