"""
PROBLEM: Contains Duplicate (LeetCode 217)
-------------------------------------------
Given an integer array `nums`, return `true` if any value appears at least twice in the array, 
and return `false` if every element is distinct.

COMMON VARIATIONS:
-------------------------------------------
1.  **Contains Duplicate II**: Find duplicates within `k` distance indices.
2.  **Contains Duplicate III**: Find duplicates within `k` distance and value difference `t`.
3.  **Find the Duplicate Number**: (Floyd's Cycle Detection) if 1 duplicate in 1..n range.

EXPLANATION (Hash Set Approach):
-------------------------------------------
1.  **Naive**: Nested loop is O(n^2).
2.  **Sorting**: Sort and check neighbors. O(n log n).
3.  **Hash Set (Optimal)**:
    - Iterate through the array.
    - Check if the current number is already in our Set.
    - If yes -> Return True.
    - If no -> Add to Set.
    - If loop finishes -> Return False.
    - Time: O(n), Space: O(n).

PSEUDOCODE:
-------------------------------------------
Function contains_duplicate(nums):
    Create empty Set `seen`

    For `num` in `nums`:
        If `num` in `seen`:
            Return True
        Add `num` to `seen`
    
    Return False
"""

from typing import List

# One-liner solution
def contains_duplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

if __name__ == "__main__":
    print("--- Testing Contains Duplicate ---")
    
    # Test Case 1: Duplicates exist
    nums1 = [1, 2, 3, 1]
    assert contains_duplicate(nums1) == True
    print(f"Test 1 Passed: {nums1} -> True")

    # Test Case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    assert contains_duplicate(nums2) == False
    print(f"Test 2 Passed: {nums2} -> False")

    # Test Case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert contains_duplicate(nums3) == True
    print(f"Test 3 Passed: {nums3} -> True")
