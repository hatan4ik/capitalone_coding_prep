"""
PROBLEM: Contains Duplicate (LeetCode 217)
--------------------------------------------------------------------------------
Given an integer array `nums`, return `true` if any value appears at least twice 
in the array, and return `false` if every element is distinct.

CAPITAL ONE INTERVIEW FOCUS:
--------------------------------------------------------------------------------
This is a fundamental data quality check. In banking, detecting duplicate 
transactions (idempotency keys), user record deduplication, or finding repeating 
patterns in fraud detection often relies on Hash Set logic for O(1) lookups.
Efficiently handling large datasets (1M+ transactions) is critical.

MOCK INTERVIEW PROMPT:
--------------------------------------------------------------------------------
"Act as a Senior Engineer at Capital One. I am solving 'Contains Duplicate'. 
Assess my ability to explain the Time/Space trade-offs between Sorting O(NlogN) 
vs Hash Set O(N). Ask me about handling large streams of data where memory 
might be a constraint."

PSEUDOCODE:
--------------------------------------------------------------------------------
Function contains_duplicate(nums):
    # 1. Create a Set to store unique elements we've seen
    seen_set = empty_set

    # 2. Iterate through each number in the input list
    For number in nums:
        # 3. Check if number is already in the set
        If number in seen_set:
            Return True  # Duplicate found
        
        # 4. Add number to set
        Add number to seen_set
    
    # 5. If loop finishes without returning, no duplicates exist
    Return False

COMPLEXITY:
--------------------------------------------------------------------------------
- Time: O(n) - We scan the array once. Set lookups are O(1) on average.
- Space: O(n) - We might store all elements in the set if no duplicates exist.
"""

from typing import List

# ------------------------------------------------------------------------------
# 1. SHORTEST PYTHON 3 ONE-LINER
# ------------------------------------------------------------------------------
def contains_duplicate_oneliner(nums: List[int]) -> bool:
    """Returns True if duplicates exist, False otherwise."""
    return len(set(nums)) != len(nums)

# ------------------------------------------------------------------------------
# 2. STANDARD READABLE SOLUTION (Interview Safe)
# ------------------------------------------------------------------------------
def contains_duplicate(nums: List[int]) -> bool:
    """
    Standard solution using a Hash Set for O(n) time complexity.
    Preferred in interviews to demonstrate understanding of logic.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# ------------------------------------------------------------------------------
# RELATED CAPITAL ONE / LEETCODE VARIATIONS
# ------------------------------------------------------------------------------
# 1. Contains Duplicate II (LeetCode 219): 
#    - Find duplicates within k distance. 
#    - Use a Sliding Window with a Set.
#
# 2. Find the Duplicate Number (LeetCode 287): 
#    - Array contains n+1 integers in range [1, n].
#    - Solved using Floyd's Tortoise and Hare (Cycle Detection) for O(1) space.
#
# 3. Design Hash Set (LeetCode 705):
#    - Implement the data structure backing this solution.

if __name__ == "__main__":
    print("--- Testing Contains Duplicate ---")
    
    # Test Case 1: Duplicates exist
    nums1 = [1, 2, 3, 1]
    assert contains_duplicate_oneliner(nums1) == True
    print(f"Test 1 Passed: {nums1} -> True")

    # Test Case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    assert contains_duplicate(nums2) == False
    print(f"Test 2 Passed: {nums2} -> False")

    # Test Case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert contains_duplicate_oneliner(nums3) == True
    print(f"Test 3 Passed: {nums3} -> True")