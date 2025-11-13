class BankAccount:
    """
    Simple bank account model that supports deposits, withdrawals, and balance checks.

    Attributes:
        owner (str): Account holder's name.
        balance (float): Current balance of the account.
    """

    def __init__(self, owner: str, opening_balance: float = 0.0) -> None:
        """Create a bank account with an owner and optional opening balance."""
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.owner = owner
        self.balance = float(opening_balance)

    def deposit(self, amount: float) -> None:
        """
        Add funds to the account.

        Args:
            amount (float): The amount of money to deposit. Must be positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Remove funds from the account if sufficient balance exists.

        Args:
            amount (float): The amount to withdraw. Must be positive and
                less than or equal to current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self) -> float:
        """Return the current account balance."""
        return self.balance


if __name__ == "__main__":
    # Demonstration of the BankAccount class usage.
    account = BankAccount("Jordan", 100.0)

    # Deposit funds and report the balance.
    account.deposit(50.0)
    print(f"Balance after deposit: {account.get_balance():.2f}")

    # Withdraw funds and report the balance.
    account.withdraw(30.0)
    print(f"Balance after withdrawal: {account.get_balance():.2f}")

    # Show final balance, highlighting the available method usage.
    print(f"Final balance for {account.owner}: {account.get_balance():.2f}")

