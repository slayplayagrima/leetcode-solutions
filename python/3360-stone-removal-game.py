# LeetCode 3360. Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/
# Difficulty: Easy
# Language: Python3
# Submission: 2203895682
# Submitted: 2026-11-26 12:49:30 UTC
# Runtime: 0 ms, Memory: 19.2 MB

class Solution:
    def canAliceWin(self, n: int) -> bool:
        take, k = 10, 0
        while n >= take:
            n -= take
            take -= 1
            k += 1
        return k % 2 == 1
