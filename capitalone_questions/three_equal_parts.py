"""
PROBLEM: Three Equal Parts (LeetCode 927)
-------------------------------------------
You are given an array `arr` consisting of 0s and 1s.
Divide the array into 3 non-empty parts such that all of them represent the same binary value.
Return indices `[i, j]` where:
1.  Part 1: arr[0...i]
2.  Part 2: arr[i+1...j-1]
3.  Part 3: arr[j...length-1]

If not possible, return [-1, -1].

COMMON VARIATIONS:
-------------------------------------------
1.  **Integer Array (Equal Sum)**: Partition array into 3 parts with equal *sum* (LeetCode 1013).
    *   *Difference*: Easier. Just check total sum % 3 == 0, then greedily find cumulative sums.
2.  **String Partitioning**: Given a string of digits, split into 3 numbers that are equal.
3.  **Binary String**: Same as this problem but input is a string "10101".

EXPLANATION:
-------------------------------------------
1.  **Count 1s**: The number of 1s must be divisible by 3. If `total_ones % 3 != 0`, it's impossible.
2.  **Target 1s**: Each part must have `k = total_ones / 3` ones.
3.  **Find "Anchors"**:
    *   Find the index of the *first* "1" in Part 1 (`start`).
    *   Find the index of the *first* "1" in Part 2 (`mid`).
    *   Find the index of the *first* "1" in Part 3 (`end`).
4.  **Compare**:
    *   The bit pattern starting from `start`, `mid`, and `end` must be identical until the end of the array.
    *   The number of zeros *after* the last 1 in Part 3 dictates how many trailing zeros Parts 1 and 2 must accommodate.
5.  **Validation**:
    *   We match bits. If `arr[start] == arr[mid] == arr[end]` implies the significant parts match.
    *   We increment pointers until we hit the end of the array (driven by Part 3).

PSEUDOCODE:
-------------------------------------------
Function three_equal_parts(arr):
    `count` = count(1s in arr)
    If `count` % 3 != 0: Return [-1, -1]
    If `count` == 0: Return [0, 2] (Any split works for all zeros)

    `k` = `count` / 3
    Find index `i1` of 1st one
    Find index `i2` of (k+1)th one
    Find index `i3` of (2k+1)th one

    While `i3` < length of arr:
        If `arr[i1]` != `arr[i2]` OR `arr[i2]` != `arr[i3]`:
            Return [-1, -1]
        Increment `i1`, `i2`, `i3`

    Return [`i1` - 1, `i2`] (Adjust indices for split points)
"""

from typing import List

def three_equal_parts(arr: List[int]) -> List[int]:
    total_ones = sum(arr)
    
    # 1. Quick Failure Checks
    if total_ones % 3 != 0:
        return [-1, -1]
    
    # 2. Handle All Zeros case
    if total_ones == 0:
        return [0, len(arr) - 1] # Valid split for [0, 0, 0] is i=0, j=2
        
    k = total_ones // 3
    
    # 3. Find starting indices of the 1st, (k+1)th, and (2k+1)th ones
    i1, i2, i3 = -1, -1, -1
    count = 0
    
    for idx, x in enumerate(arr):
        if x == 1:
            count += 1
            if count == 1:
                i1 = idx
            elif count == k + 1:
                i2 = idx
            elif count == 2 * k + 1:
                i3 = idx

    # 4. Compare partitions pixel by pixel
    # We drive the loop using i3 because Part 3 extends to the very end of the array.
    while i3 < len(arr):
        if arr[i1] == arr[i2] == arr[i3]:
            i1 += 1
            i2 += 1
            i3 += 1
        else:
            return [-1, -1]
            
    # 5. Return split points
    # i1 is now at the start of Part 2 (after incrementing past Part 1's trailing zeros)
    # i2 is now at the start of Part 3
    return [i1 - 1, i2]

"""
VARIATION: Partition Array Into Three Parts With Equal Sum (LeetCode 1013)
This is the simpler integer version often used as a warm-up.
"""
def can_three_parts_equal_sum(arr: List[int]) -> bool:
    total = sum(arr)
    if total % 3 != 0:
        return False
        
    target = total // 3
    current_sum = 0
    parts_found = 0
    
    for num in arr:
        current_sum += num
        if current_sum == target:
            parts_found += 1
            current_sum = 0
            
    # We need at least 3 parts. 
    # (parts_found >= 3 handles cases where 0s exist between parts)
    return parts_found >= 3