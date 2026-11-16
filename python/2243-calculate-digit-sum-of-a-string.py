# LeetCode 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# Difficulty: Easy
# Language: Python3
# Submission: 2197474484
# Submitted: 2026-11-16 17:11:43 UTC
# Runtime: 0 ms, Memory: 19.1 MB

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []  # The array representing the string after each round
            n = len(s)
            for i in range(0, n, k):
                val = 0
                for j in range(i, min(i + k, n)):
                    val += int(s[j])
                tmp.append(str(val))
            s = "".join(tmp)
        return s
