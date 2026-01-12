"""
PROBLEM: Simple Bank System (LeetCode 2043)
-------------------------------------------
You have been tasked with writing a program for a popular bank that will automate all its 
incoming transactions (transfer, deposit, and withdraw).

EXPLANATION:
-------------------------------------------
1.  **Data Structure**: We use a direct list (array) `balance` to store the money for each account.
    The account `i` (1-indexed) corresponds to `balance[i-1]` (0-indexed).
2.  **Validation**: All operations first verify if the account number is valid (between 1 and n).
3.  **Logic**:
    - **Transfer**: specific checks for valid accounts and sufficient funds. Updates both sender and receiver.
    - **Deposit**: Adds money if account exists.
    - **Withdraw**: Deducts money if account exists and has funds.
    - All operations return `True` on success, `False` otherwise.

PSEUDOCODE:
-------------------------------------------
Class Bank:
    Function init(balance[]):
        this.balance = balance
        this.n = length of balance

    Function transfer(account1, account2, money):
        If NOT (1 <= account1 <= n) OR NOT (1 <= account2 <= n): Return False
        If balance[account1] < money: Return False
        
        balance[account1] -= money
        balance[account2] += money
        Return True

    Function deposit(account, money):
        If NOT (1 <= account <= n): Return False
        
        balance[account] += money
        Return True

    Function withdraw(account, money):
        If NOT (1 <= account <= n): Return False
        If balance[account] < money: Return False
        
        balance[account] -= money
        Return True
"""

class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Check if accounts are valid (1-indexed)
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        
        # Check for sufficient funds
        if self.balance[account1 - 1] < money:
            return False
            
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Check if account is valid
        if not (1 <= account <= self.n):
            return False
            
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Check if account is valid
        if not (1 <= account <= self.n):
            return False

        # Check for sufficient funds
        if self.balance[account - 1] < money:
            return False
            
        self.balance[account - 1] -= money
        return True
