"""
PROBLEM: Maximum Sum Subarray of Size K
-------------------------------------------
Given an array of integers `arr` and a positive integer `k`, find the maximum sum of any 
contiguous subarray of size `k`.

COMMON VARIATIONS (Capital One Context):
-------------------------------------------
1.  **Maximum Average Subarray** (LeetCode 643): Find max average instead of sum.
2.  **Minimum Sum Subarray**: Find min sum of size k.
3.  **Kadane's Algorithm** (LeetCode 53): Find max sum subarray of *variable* size (handling negatives).
4.  **Transaction Alerts**: Raise alert if sum of transactions in last `k` days exceeds threshold.

EXPLANATION (Sliding Window):
-------------------------------------------
1.  **Naive**: Calculate sum for every subarray of size k. O(n*k). Too slow.
2.  **Sliding Window (Optimal)**:
    - Compute sum of first `k` elements.
    - Slide the window one step to the right:
        - Subtract the element leaving the window (left).
        - Add the element entering the window (right).
    - Update max sum.
    - Time: O(n), Space: O(1).

PSEUDOCODE:
-------------------------------------------
Function max_subarray_sum(arr, k):
    If length(arr) < k:
        Return Error or 0

    current_sum = Sum of arr[0...k-1]
    max_sum = current_sum

    For i from k to length(arr) - 1:
        current_sum += arr[i] - arr[i - k]
        max_sum = Max(max_sum, current_sum)
    
    Return max_sum
"""

from typing import List

# One-liner solution
def max_subarray_sum(arr: List[int], k: int) -> int:
    return max(sum(arr[i:i+k]) for i in range(len(arr)-k+1))

if __name__ == "__main__":
    print("--- Testing Maximum Sum Subarray (Size K) ---")
    
    # Test 1
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    # Subarrays: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6
    # Max is 9
    assert max_subarray_sum(arr1, k1) == 9
    print(f"Test 1 Passed: {arr1}, k={k1} -> 9")
    
    # Test 2
    arr2 = [2, 3, 4, 1, 5]
    k2 = 2
    # [2,3]=5, [3,4]=7, [4,1]=5, [1,5]=6
    # Max is 7
    assert max_subarray_sum(arr2, k2) == 7
    print(f"Test 2 Passed: {arr2}, k={k2} -> 7")