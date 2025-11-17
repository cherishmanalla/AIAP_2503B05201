def discount(price, category):
    """
    Return the discounted price based on the customer category.

    Rules
    -----
    student:
        - price > 1000  -> 10% discount
        - otherwise     -> 5% discount
    regular (default):
        - price > 2000  -> 15% discount
        - otherwise     -> no discount
    """

    def student_discount(amount):
        return amount * 0.9 if amount > 1000 else amount * 0.95

    def regular_discount(amount):
        return amount * 0.85 if amount > 2000 else amount

    strategies = {
        "student": student_discount,
        # any non-student category uses the regular rule set
    }

    discount_fn = strategies.get(category.lower(), regular_discount)
    return discount_fn(price)


if __name__ == "__main__":
    try:
        entered_price = float(input("Enter price: ").strip())
    except ValueError:
        raise ValueError("Price must be a numeric value.")

    entered_category = input('Enter category (e.g., "student"): ').strip()
    final_price = discount(entered_price, entered_category)
    print(f"Discounted price: {final_price}")
