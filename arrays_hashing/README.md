# Arrays & Hashing

This category is the foundation of algorithmic interviews at Capital One. These problems test your ability to efficiently manipulate data structures and use hashing for O(1) lookups, which is critical for processing large datasets (transaction logs, user records) common in banking.

## Key Concepts
- **Hash Maps (Dictionaries)**: O(1) average time for insertion and lookup. Key for "frequency" or "existence" checks.
- **Hash Sets**: O(1) check for duplicates.
- **Prefix Sums**: Pre-computing sums to answer range queries quickly.

## Essential Problems

### 1. Two Sum (LeetCode 1)
**Goal**: Find indices of two numbers that add up to a target.
- **Why it's asked**: Tests basic Hash Map usage vs. Brute Force.
- **Solution**: [Python Code](./two_sum.py)
- **Key Insight**: Store `value: index` in a map. Check if `target - current_value` exists.

### 2. Contains Duplicate (LeetCode 217)
**Goal**: Check if any value appears at least twice.
- **Why it's asked**: Basic data validation logic.
- **Solution**: [Python Code](./contains_duplicate.py)
- **Key Insight**: Use a Hash Set. If element is seen before, return True.

### 3. Valid Anagram (LeetCode 242)
**Goal**: Check if two strings use the same characters with same frequencies.
- **Why it's asked**: String manipulation + Hashing basics.
- **Solution**: [Python Code](./valid_anagram.py)
- **Approach**: Use a frequency map (or array of size 26 for English letters). Count chars in `s`, decrement for `t`. All counts must be 0.

### 4. Group Anagrams (LeetCode 49)
**Goal**: Group strings that are anagrams.
- **Key Insight**: Sort each string to use as a key, or use a character count tuple `(count_a, count_b, ...)` as the key in a Hash Map.

## Study Guide for Capital One
- **Focus on Edge Cases**: Empty arrays, arrays with 1 element, negative numbers.
- **Explain your approach**: Always mention "I will use a Hash Map to trade space for time, reducing complexity from O(n^2) to O(n)."
- **Code Cleanliness**: Use meaningful variable names (`seen`, `freq_map`, `char_count`) instead of `d`, `h`, `m`.

## How to Run the Code
You can run the provided solutions directly to see the tests pass:

```bash
python3 two_sum.py
python3 contains_duplicate.py
```
