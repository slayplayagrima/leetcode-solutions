# LeetCode 4078. Three Fibonacci Sum
# https://leetcode.com/problems/three-fibonacci-sum/
# Difficulty: Easy
# Language: Python3
# Submission: 2183130196
# Submitted: 2026-10-27 14:03:33 UTC
# Runtime: 1 ms, Memory: 19.1 MB

class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b, c = 0, 1, 1
        while a + b + c < n:
            a, b, c = b, c, b + c
        return a + b + c == n
