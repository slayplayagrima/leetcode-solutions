# LeetCode 2161. Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/
# Difficulty: Medium
# Language: Python3
# Submission: 2184070748
# Submitted: 2026-10-28 16:23:47 UTC
# Runtime: 36 ms, Memory: 33.5 MB

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        if n==1: return nums
        R=[]
        l, m=0, 0
        for x in nums:
            if x<pivot:
                nums[l]=x
                l+=1
            elif x>pivot:
                R.append(x)
            else:
                m+=1
        return nums[:l]+[pivot]*m+R
        
