"""
PROBLEM: Two Sum (LeetCode 1)
-------------------------------------------
Given an array of integers `nums` and an integer `target`, return indices of the two numbers 
such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

COMMON VARIATIONS (Capital One / FAANG Context):
-------------------------------------------
1.  **Input Sorted?** (Two Sum II): Use Two Pointers (Left/Right) for O(1) space.
2.  **Return Values?**: Sometimes asked to return the *values* instead of indices.
3.  **Multiple Pairs?**: Find *all* unique pairs that sum to target.
4.  **Closest Sum?**: Find two numbers summing closest to target.

EXPLANATION (Hash Map Approach):
-------------------------------------------
1.  **Naive**: A nested loop checking every pair is O(n^2). Too slow.
2.  **Optimized**: Use a Hash Map (Dictionary) to "remember" numbers we've seen.
3.  **Logic**: 
    - As we iterate through `nums`, for each `num`, we calculate `diff = target - num`.
    - If `diff` is already in our map, we found the pair! Return `[map[diff], current_index]`.
    - Otherwise, store `num` in the map with its index.
    - This allows O(n) Time Complexity and O(n) Space Complexity.

PSEUDOCODE:
-------------------------------------------
Function two_sum(nums, target):
    Create empty Map `seen` (maps value -> index)

    For index `i`, value `num` in `nums`:
        `diff` = `target` - `num`

        If `diff` exists in `seen`:
            Return [`seen[diff]`, `i`]
        
        Store `seen[num]` = `i`
    
    Return Empty List (or Error if guaranteed solution)
"""

from typing import List

# One-liner solution
def two_sum(nums: List[int], target: int) -> List[int]:
    return next(([seen[target-n], i] for i, n in enumerate(nums) if (target-n) in (seen := seen if 'seen' in locals() else {}) or not seen.update({n: i})), [])

"""
VARIATION IMPLEMENTATION: Two Sum II (Input is Sorted)
------------------------------------------------------
If the array is already sorted, we can use Two Pointers for O(1) space.
"""
# One-liner solution
def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    return [(l, r) for l in range(len(nums)) for r in range(l+1, len(nums)) if nums[l] + nums[r] == target][0] if any(nums[l] + nums[r] == target for l in range(len(nums)) for r in range(l+1, len(nums))) else []

if __name__ == "__main__":
    # Test Cases for Standard Two Sum
    print("--- Testing Two Sum (Hash Map) ---")
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("Two Sum Tests Passed!")

    # Test Cases for Sorted Two Sum
    print("\n--- Testing Two Sum II (Two Pointers) ---")
    assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_sorted([2, 3, 4], 6) == (0, 2)
    print("Two Sum Sorted Tests Passed!")