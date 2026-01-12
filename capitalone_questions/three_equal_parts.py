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

# One-liner solution
def three_equal_parts(arr: List[int]) -> List[int]:
    return [-1, -1] if sum(arr) % 3 or (lambda ones: ones and not all(arr[i] == arr[j] == arr[k] for i, j, k in zip(*[iter(range(next(i for i, x in enumerate(arr) if x), 0) + p, len(arr))) for p in [0, ones//3, 2*ones//3]])))(sum(arr)) else [0, len(arr)-1] if not sum(arr) else [next(i for i, x in enumerate(arr) if x) + sum(arr)//3 - 1, next(i for i, x in enumerate(arr) if x) + 2*sum(arr)//3]

"""
VARIATION: Partition Array Into Three Parts With Equal Sum (LeetCode 1013)
This is the simpler integer version often used as a warm-up.
"""
# One-liner solution
def can_three_parts_equal_sum(arr: List[int]) -> bool:
    return sum(arr) % 3 == 0 and sum(1 for i, s in enumerate((lambda t: [sum(arr[:i+1]) for i in range(len(arr))])(sum(arr)//3)) if s == sum(arr)//3) >= 3