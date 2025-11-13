def print_multiples(number: int) -> None:
    """Print the first 10 multiples of the provided number."""
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


def print_multiples_with_while(number: int) -> None:
    """Print the first 10 multiples using a while loop (alternate approach)."""
    count = 1
    while count <= 10:
        print(f"{number} x {count} = {number * count}")
        count += 1


if __name__ == "__main__":
    print("Using for loop:")
    print_multiples(5)

    print("\nUsing while loop:")
    print_multiples_with_while(5)

