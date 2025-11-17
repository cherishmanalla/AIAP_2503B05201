class ShoppingCart:
    """Simple in-memory shopping cart."""

    def __init__(self):
        self.items = {}  # name -> price

    def add_item(self, name, price):
        """Adds/updates an item with given name and price."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        self.items[name] = float(price)

    def remove_item(self, name):
        """Removes an item by name, raises if missing."""
        if name not in self.items:
            raise KeyError(f"{name} not in cart")
        del self.items[name]

    def total_cost(self):
        """Returns total cost of cart items."""
        return round(sum(self.items.values()), 2)


def test_shopping_cart():
    """AI-generated tests for ShoppingCart."""
    cart = ShoppingCart()

    # Add single item
    cart.add_item("Apple", 1.50)
    assert cart.total_cost() == 1.5

    # Add multiple items
    cart.add_item("Bread", 2.25)
    cart.add_item("Milk", 3.40)
    assert cart.total_cost() == 7.15

    # Update existing item (price change)
    cart.add_item("Bread", 2.50)
    assert cart.total_cost() == 7.40

    # Remove item
    cart.remove_item("Apple")
    assert cart.total_cost() == 5.9

    # Remove remaining items
    cart.remove_item("Bread")
    cart.remove_item("Milk")
    assert cart.total_cost() == 0

    # Add zero-priced item
    cart.add_item("Coupon", 0)
    assert cart.total_cost() == 0

    # Validate errors
    try:
        cart.add_item("", 1)
        assert False, "Empty name should fail"
    except ValueError:
        pass

    try:
        cart.add_item("Orange", -1)
        assert False, "Negative price should fail"
    except ValueError:
        pass

    try:
        cart.remove_item("Missing")
        assert False, "Removing missing item should fail"
    except KeyError:
        pass

    print("All ShoppingCart tests passed! ✓")


if __name__ == "__main__":
    test_shopping_cart()
    print("\nFull class with tested functionalities ✓")

