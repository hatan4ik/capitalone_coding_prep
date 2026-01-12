"""
Problem: Maximum Sum Subarray of Size K
Find the maximum sum of a subarray with size k.

Pseudocode:
- Use a window of size k
- Slide window and update max sum
"""
def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
