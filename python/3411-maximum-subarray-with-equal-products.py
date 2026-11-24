# LeetCode 3411. Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/
# Difficulty: Easy
# Language: Python3
# Submission: 2202785220
# Submitted: 2026-11-24 18:14:22 UTC
# Runtime: 9 ms, Memory: 19 MB

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            prod_val = nums[i]
            gcd_val = nums[i]
            lcm_val = nums[i]
            for j in range(i + 1, len(nums)):
                prod_val = prod_val * nums[j]
                gcd_val = gcd(gcd_val, nums[j])
                lcm_val = lcm(lcm_val, nums[j])
                if prod_val > gcd_val * lcm_val:
                    break
                if prod_val == gcd_val * lcm_val:
                    res = max(res, j - i + 1)
        return res
