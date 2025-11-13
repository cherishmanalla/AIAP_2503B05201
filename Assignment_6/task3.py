def classify_age(age: int) -> str:
    """
    Classify the provided age using nested if-elif-else blocks.

    Returns one of: "infant", "child", "teen", "adult", "senior".
    Raises:
        ValueError: If the age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age <= 2:
        category = "infant"
    else:
        if age <= 12:
            category = "child"
        else:
            if age <= 19:
                category = "teen"
            else:
                if age <= 64:
                    category = "adult"
                else:
                    category = "senior"

    return category


def classify_age_with_guard(age: int) -> str:
    """
    Alternative classification using guard-style early returns.

    This demonstrates the same logic without nested blocks.
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age <= 2:
        return "infant"
    if age <= 12:
        return "child"
    if age <= 19:
        return "teen"
    if age <= 64:
        return "adult"
    return "senior"


if __name__ == "__main__":
    sample_ages = [0, 4, 16, 35, 70]
    print("Nested if-elif-else classification:")
    for sample in sample_ages:
        print(f"Age {sample}: {classify_age(sample)}")

    print("\nGuarded conditional classification:")
    for sample in sample_ages:
        print(f"Age {sample}: {classify_age_with_guard(sample)}")

