""" 
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # edge case
        if s == '':
            return True
        # 1st: determine if s is a subset of t
        set_s = set(s)
        set_t = set(t)
        if not set_s.issubset(t):
            return False
        # 2nd: Check to see if order was respected
        for letter in t:
            # Itterate through the larger set to see if we have the subset in the right order
            # Pop letters from original string as we go while S still has characters
            if not s:
                return True
            if s[0] == letter:
                s = s[1:]
        return not bool(s)