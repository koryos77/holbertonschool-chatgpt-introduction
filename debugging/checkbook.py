class Checkbook:
    """
    A class to represent a simple checkbook where users can deposit, withdraw, and check their balance.

    Attributes:
    balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes a new checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.
        
        Parameters:
        amount (float): The amount to deposit into the checkbook.
        
        Returns:
        None: This method doesn't return anything. It updates the balance directly.
        
        Prints:
        - A message confirming the deposit.
        - The updated balance after the deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if there are sufficient funds.
        
        Parameters:
        amount (float): The amount to withdraw from the checkbook.
        
        Returns:
        None: This method doesn't return anything. It updates the balance directly.
        
        Prints:
        - A message confirming the withdrawal if successful.
        - The updated balance after the withdrawal.
        - An error message if there are insufficient funds.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        
        Parameters:
        None
        
        Returns:
        None: This method only prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook. It allows the user to perform actions such as deposit,
    withdrawal, or check balance.

    The function keeps running until the user decides to exit.
    """
    cb = Checkbook()  # Create a new Checkbook instance
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        # Exit the loop if the user types 'exit'
        if action.lower() == 'exit':
            break
        
        # Handle deposit action
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a valid numeric value for deposit.")
        
        # Handle withdrawal action
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a valid numeric value for withdrawal.")
        
        # Handle balance check action
        elif action.lower() == 'balance':
            cb.get_balance()
        
        # Handle invalid command
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    """
    Entry point of the program. This will execute the main function to interact with the user.
    """
    main()
