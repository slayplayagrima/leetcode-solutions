# LeetCode 3644. Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
# Difficulty: Medium
# Language: Python3
# Submission: 2179927538
# Submitted: 2026-10-23 18:23:34 UTC
# Runtime: 28 ms, Memory: 32.1 MB

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i in range(n):
            if nums[i] == i:
                continue
            res &= nums[i]
        return 0 if res == -1 else res
