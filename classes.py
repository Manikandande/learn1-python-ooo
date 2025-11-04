
class BankAccount:
    # Class variable shared by all instances
    bank_name = "OpenAI Bank"

    def __init__(self, owner, balance=0):
        """Initialize the account with an owner and optional starting balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if funds are sufficient."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        """Display the current balance."""
        print(f"{self.owner}'s account balance: ${self.balance}")

# Example usage
if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()

    # Accessing a class variable
    print("Bank Name:", BankAccount.bank_name)
