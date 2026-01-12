# Sliding Window

The Sliding Window technique is essential for problems involving arrays or strings where you need to calculate something over a subset of data (a window) that moves across the input.

In a **Capital One** interview context, this often maps to analyzing time-series data, such as:
- "Find the highest spending period of 3 days."
- "Detect fraud patterns in a stream of transactions."

## Key Concepts
- **Fixed Size Window**: The window size `k` is constant. (e.g., Max sum of size 3).
- **Variable Size Window**: The window grows/shrinks to satisfy a condition. (e.g., Longest substring without repeating characters).

## Essential Problems

### 1. Maximum Sum Subarray of Size K
**Goal**: Find the max sum of a contiguous subarray of fixed size `k`.
- **Solution**: [Python Code](./max_subarray_sum.py)
- **Key Insight**: Don't recompute the sum from scratch. `NewSum = OldSum - Leaving + Entering`.
- **Complexity**: O(n) Time, O(1) Space.

### 2. Longest Substring Without Repeating Characters (LeetCode 3)
**Goal**: Find the length of the longest substring with unique characters.
- **Key Insight**: Use a generic Variable Size window with a Hash Set/Map to track characters in the current window.

## Study Guide
- **Identification**: Look for keywords like "contiguous subarray", "substring", "consecutive elements".
- **Optimization**: The goal is almost always to turn a nested loop O(n^2) or O(n*k) solution into a linear O(n) solution.
