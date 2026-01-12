# Capital One Software Architect Interview Guide

## Overview
This guide covers common coding patterns and problems frequently asked in Capital One software architect interviews, with detailed pseudocode explanations and variations.

---

## 1. Array & Hashing Problems

### Two Sum (LeetCode 1) - **VERY COMMON**

**Problem**: Given an array and target, find two numbers that sum to target.

**Pseudocode**:
```
Function two_sum(nums, target):
    seen = empty_map()
    
    For i, num in nums:
        diff = target - num
        If diff in seen:
            Return [seen[diff], i]
        seen[num] = i
    
    Return []
```

**Variations Asked**:
- **Two Sum II**: Array is sorted → Use two pointers
- **Three Sum**: Find triplets that sum to zero
- **Two Sum Closest**: Find pair with sum closest to target
- **Two Sum All Pairs**: Return all unique pairs

**Code Snippet**:
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

---

## 2. Banking/Financial System Design

### Simple Bank System (LeetCode 2043) - **CAPITAL ONE FAVORITE**

**Problem**: Design a bank system with transfer, deposit, withdraw operations.

**Pseudocode**:
```
Class Bank:
    Function init(balances):
        this.balances = balances
        this.n = length(balances)
    
    Function transfer(from, to, amount):
        If NOT valid_accounts(from, to): Return False
        If balances[from-1] < amount: Return False
        
        balances[from-1] -= amount
        balances[to-1] += amount
        Return True
    
    Function deposit(account, amount):
        If NOT valid_account(account): Return False
        balances[account-1] += amount
        Return True
    
    Function withdraw(account, amount):
        If NOT valid_account(account): Return False
        If balances[account-1] < amount: Return False
        balances[account-1] -= amount
        Return True
```

**Variations Asked**:
- **Transaction History**: Add logging for all operations
- **Interest Calculation**: Add compound interest features
- **Account Types**: Different account types (checking, savings)
- **Overdraft Protection**: Allow negative balances with fees
- **Concurrent Access**: Thread-safe operations

---

## 3. Advanced Array Problems

### Three Equal Parts (LeetCode 927) - **CHALLENGING**

**Problem**: Divide binary array into 3 parts representing same binary value.

**Pseudocode**:
```
Function three_equal_parts(arr):
    ones_count = count_ones(arr)
    If ones_count % 3 != 0: Return [-1, -1]
    If ones_count == 0: Return [0, len(arr)-1]
    
    k = ones_count / 3
    Find positions of 1st, (k+1)th, (2k+1)th ones
    
    While comparing all three parts:
        If parts don't match: Return [-1, -1]
        Move all pointers forward
    
    Return split_indices
```

**Variations**:
- **Equal Sum Parts**: Divide into 3 parts with equal sum
- **K Equal Parts**: Generalize to K parts
- **String Version**: Same logic with string input

---

## 4. Sliding Window Problems

### Maximum Subarray Sum of Size K

**Pseudocode**:
```
Function max_subarray_sum(arr, k):
    window_sum = sum(arr[0:k])
    max_sum = window_sum
    
    For i from k to len(arr):
        window_sum += arr[i] - arr[i-k]  // Slide window
        max_sum = max(max_sum, window_sum)
    
    Return max_sum
```

**Variations**:
- **Variable Window Size**: Find optimal window size
- **Minimum Window**: Find minimum sum window
- **Longest Substring**: Without repeating characters

---

## 5. System Design Patterns (Common in Capital One)

### LRU Cache (LeetCode 146) - **VERY IMPORTANT**

**Pseudocode**:
```
Class LRUCache:
    Function init(capacity):
        this.capacity = capacity
        this.cache = HashMap()
        this.dll = DoublyLinkedList()  // Most recent at head
    
    Function get(key):
        If key in cache:
            Move node to head
            Return value
        Return -1
    
    Function put(key, value):
        If key exists:
            Update value, move to head
        Else:
            If at capacity: Remove tail
            Add new node at head
```

**Capital One Variations**:
- **TTL Cache**: Add time-to-live expiration
- **Weighted LRU**: Different weights for different items
- **Multi-level Cache**: L1, L2 cache hierarchy

---

## 6. Tree & Graph Problems

### Binary Tree Maximum Path Sum (LeetCode 124)

**Pseudocode**:
```
Function max_path_sum(root):
    max_sum = -infinity
    
    Function dfs(node):
        If node is null: Return 0
        
        left_gain = max(0, dfs(node.left))
        right_gain = max(0, dfs(node.right))
        
        current_max = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_max)
        
        Return node.val + max(left_gain, right_gain)
    
    dfs(root)
    Return max_sum
```

---

## 7. Dynamic Programming

### Coin Change (LeetCode 322) - **FINANCIAL CONTEXT**

**Pseudocode**:
```
Function coin_change(coins, amount):
    dp = array of size (amount + 1) filled with infinity
    dp[0] = 0
    
    For i from 1 to amount:
        For coin in coins:
            If coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    Return dp[amount] if dp[amount] != infinity else -1
```

**Capital One Context**: Currency exchange, transaction fees, payment processing

---

## 8. String Processing

### Valid Parentheses (LeetCode 20)

**Pseudocode**:
```
Function is_valid(s):
    stack = empty_stack()
    mapping = {'(': ')', '[': ']', '{': '}'}
    
    For char in s:
        If char is opening bracket:
            Push char to stack
        Else:
            If stack is empty OR mapping[stack.top()] != char:
                Return False
            Pop from stack
    
    Return stack is empty
```

---

## 9. Interview Strategy & Tips

### Problem-Solving Framework
1. **Clarify Requirements** (2-3 minutes)
   - Ask about edge cases
   - Confirm input/output format
   - Discuss constraints

2. **High-Level Approach** (3-5 minutes)
   - Explain your strategy
   - Discuss time/space complexity
   - Consider alternatives

3. **Implementation** (15-20 minutes)
   - Start with pseudocode if complex
   - Code incrementally
   - Test with examples

4. **Testing & Optimization** (5-10 minutes)
   - Walk through test cases
   - Discuss improvements
   - Handle edge cases

### Capital One Specific Tips
- **Financial Context**: Many problems have banking/finance themes
- **System Design**: Be ready for design questions about scalable systems
- **Code Quality**: Clean, readable code is highly valued
- **Communication**: Explain your thought process clearly
- **Edge Cases**: Always consider boundary conditions

### Common Complexity Patterns
- **O(n) Hash Map**: Two Sum, frequency counting
- **O(n log n) Sorting**: Merge intervals, meeting rooms
- **O(n²) Nested Loops**: Brute force approaches (usually not optimal)
- **O(log n) Binary Search**: Search in sorted arrays
- **O(1) Amortized**: Hash operations, dynamic arrays

### Red Flags to Avoid
- Jumping into code without explanation
- Not considering edge cases
- Poor variable naming
- Not testing your solution
- Giving up when stuck (ask for hints)

---

## 10. Practice Problems by Category

### Arrays & Hashing (High Priority)
- Two Sum, Three Sum
- Group Anagrams
- Top K Frequent Elements
- Product of Array Except Self

### Banking/Finance Specific
- Simple Bank System
- Design ATM
- Currency Exchange
- Transaction Processing

### System Design
- LRU Cache
- Design Twitter
- Rate Limiter
- Load Balancer

### Trees & Graphs
- Binary Tree Traversals
- Validate BST
- Course Schedule (Topological Sort)
- Number of Islands

### Dynamic Programming
- Coin Change
- House Robber
- Longest Common Subsequence
- Maximum Subarray

Remember: Capital One values **clean code**, **clear communication**, and **practical problem-solving** over just getting the right answer!