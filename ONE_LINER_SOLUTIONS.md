# Python 3 One-Liner Solutions - Capital One Interview Prep

## Array & Hashing Problems

### Contains Duplicate
```python
def contains_duplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

### Valid Anagram
```python
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

### Two Sum
```python
def two_sum(nums: List[int], target: int) -> List[int]:
    return next(([seen[target-n], i] for i, n in enumerate(nums) if (target-n) in (seen := seen if 'seen' in locals() else {}) or not seen.update({n: i})), [])
```

### Two Sum (Sorted Array)
```python
def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    return [(l, r) for l in range(len(nums)) for r in range(l+1, len(nums)) if nums[l] + nums[r] == target][0] if any(nums[l] + nums[r] == target for l in range(len(nums)) for r in range(l+1, len(nums))) else []
```

## Sliding Window Problems

### Maximum Subarray Sum (Size K)
```python
def max_subarray_sum(arr: List[int], k: int) -> int:
    return max(sum(arr[i:i+k]) for i in range(len(arr)-k+1))
```

## Capital One Specific Problems

### Simple Bank System
```python
class Bank:
    def __init__(self, balance: list[int]): self.balance, self.n = balance, len(balance)
    def transfer(self, a1: int, a2: int, money: int) -> bool: return 1 <= a1 <= self.n and 1 <= a2 <= self.n and self.balance[a1-1] >= money and not (self.balance[a1-1].__isub__(money), self.balance[a2-1].__iadd__(money))[0]
    def deposit(self, account: int, money: int) -> bool: return 1 <= account <= self.n and not self.balance[account-1].__iadd__(money)
    def withdraw(self, account: int, money: int) -> bool: return 1 <= account <= self.n and self.balance[account-1] >= money and not self.balance[account-1].__isub__(money)
```

### Three Equal Parts
```python
def three_equal_parts(arr: List[int]) -> List[int]:
    return [-1, -1] if sum(arr) % 3 or (lambda ones: ones and not all(arr[i] == arr[j] == arr[k] for i, j, k in zip(*[iter(range(next(i for i, x in enumerate(arr) if x), 0) + p, len(arr))) for p in [0, ones//3, 2*ones//3]])))(sum(arr)) else [0, len(arr)-1] if not sum(arr) else [next(i for i, x in enumerate(arr) if x) + sum(arr)//3 - 1, next(i for i, x in enumerate(arr) if x) + 2*sum(arr)//3]
```

### Three Parts Equal Sum
```python
def can_three_parts_equal_sum(arr: List[int]) -> bool:
    return sum(arr) % 3 == 0 and sum(1 for i, s in enumerate((lambda t: [sum(arr[:i+1]) for i in range(len(arr))])(sum(arr)//3)) if s == sum(arr)//3) >= 3
```

## Key Python 3 One-Liner Techniques Used

1. **Walrus Operator (`:=`)** - Assignment within expressions
2. **Generator Expressions** - Memory efficient iteration
3. **List Comprehensions** - Compact list creation
4. **Lambda Functions** - Inline function definitions
5. **`next()` with generators** - First match finding
6. **`any()` and `all()`** - Boolean aggregation
7. **Tuple unpacking** - Multiple assignments
8. **Method chaining** - Fluent interfaces
9. **`__isub__()` and `__iadd__()`** - In-place operations returning None
10. **Conditional expressions** - Ternary operators

## Trade-offs of One-Liners

**Pros:**
- Extremely concise
- Shows Python mastery
- Impressive in interviews

**Cons:**
- Reduced readability
- Harder to debug
- May sacrifice performance
- Difficult to maintain

**Interview Recommendation:** Start with readable solution, then show one-liner as optimization.