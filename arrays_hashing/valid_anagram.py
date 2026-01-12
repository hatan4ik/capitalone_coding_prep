"""
PROBLEM: Valid Anagram (LeetCode 242)
-------------------------------------------
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

COMMON VARIATIONS:
-------------------------------------------
1.  **Group Anagrams**: Group a list of strings into anagrams.
2.  **Find All Anagrams in a String**: Sliding window approach.
3.  **Case Sensitivity**: Are 'A' and 'a' the same? (Usually assume distinct unless specified).

EXPLANATION (Frequency Map):
-------------------------------------------
1.  **Length Check**: If `len(s) != len(t)`, they can't be anagrams. Return False.
2.  **Sorting**: Sort both strings and compare. O(N log N). Good for space, bad for time.
3.  **Hash Map / Array (Optimal)**:
    - Count frequency of each character in `s`.
    - Decrement frequency for each character in `t`.
    - If all counts are 0, it's an anagram.
    - Time: O(N), Space: O(1) (since alphabet size is fixed at 26).

PSEUDOCODE:
-------------------------------------------
Function isAnagram(s, t):
    If length(s) != length(t):
        Return False
    
    Create Map `count` (default 0)
    
    For `char` in `s`:
        `count[char]` += 1
    
    For `char` in `t`:
        `count[char]` -= 1
        
    For `val` in `count.values()`:
        If `val` != 0:
            Return False
            
    Return True
"""

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    count = {}
    
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
            
    return True

# Alternative using Python's Counter
from collections import Counter
def is_anagram_pythonic(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    print("--- Testing Valid Anagram ---")
    
    # Test 1
    s1, t1 = "anagram", "nagaram"
    assert is_anagram(s1, t1) == True
    assert is_anagram_pythonic(s1, t1) == True
    print(f"Test 1 Passed: '{s1}', '{t1}' -> True")
    
    # Test 2
    s2, t2 = "rat", "car"
    assert is_anagram(s2, t2) == False
    print(f"Test 2 Passed: '{s2}', '{t2}' -> False")
    
    # Test 3: Different lengths
    s3, t3 = "a", "ab"
    assert is_anagram(s3, t3) == False
    print(f"Test 3 Passed: '{s3}', '{t3}' -> False")
