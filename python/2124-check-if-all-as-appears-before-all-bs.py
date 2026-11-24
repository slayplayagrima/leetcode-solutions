# LeetCode 2124. Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Difficulty: Easy
# Language: Python3
# Submission: 2202785943
# Submitted: 2026-11-24 18:15:23 UTC
# Runtime: 0 ms, Memory: 19 MB

class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        lasta = -1  # Index of the last occurrence of 'a'
        firstb = n  # Index of the first occurrence of 'b'
        for i in range(n):
            if s[i] == "a":
                lasta = max(lasta, i)
            else:
                firstb = min(firstb, i)
        return lasta < firstb
