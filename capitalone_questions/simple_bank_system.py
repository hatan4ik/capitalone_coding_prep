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

# One-liner solutions for Bank class methods
class Bank:
    def __init__(self, balance: list[int]): self.balance, self.n = balance, len(balance)
    def transfer(self, a1: int, a2: int, money: int) -> bool: return 1 <= a1 <= self.n and 1 <= a2 <= self.n and self.balance[a1-1] >= money and not (self.balance[a1-1].__isub__(money), self.balance[a2-1].__iadd__(money))[0]
    def deposit(self, account: int, money: int) -> bool: return 1 <= account <= self.n and not self.balance[account-1].__iadd__(money)
    def withdraw(self, account: int, money: int) -> bool: return 1 <= account <= self.n and self.balance[account-1] >= money and not self.balance[account-1].__isub__(money)
