# LeetCode 3693. Climbing Stairs II
# https://leetcode.com/problems/climbing-stairs-ii/
# Difficulty: Medium
# Language: Python3
# Submission: 2193354507
# Submitted: 2026-11-10 17:25:32 UTC
# Runtime: 144 ms, Memory: 33.3 MB

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = b = c = 0
        for i in range(n):
            a, b, c = b, c, min(a + 9, b + 4, c + 1) + costs[i]
        return c
