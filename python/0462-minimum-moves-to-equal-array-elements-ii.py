# LeetCode 462. Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Difficulty: Medium
# Language: Python3
# Submission: 2187990904
# Submitted: 2026-11-02 17:48:38 UTC
# Runtime: 5 ms, Memory: 20.3 MB

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def quickselect(a, k):
            while True:
                if len(a) <= 1:
                    return a[0]
                p = random.choice(a)
                lo = [x for x in a if x < p]
                if k < len(lo):
                    a = lo
                    continue
                hi = [x for x in a if x > p]
                if k >= len(a) - len(hi):
                    k -= len(a) - len(hi)
                    a = hi
                    continue
                return p  # pivot sits at position k

        med = quickselect(nums, len(nums) // 2)
        return sum(abs(x - med) for x in nums)
