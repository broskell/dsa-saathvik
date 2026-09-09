# LC 1480 — Running Sum of 1D Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Time: O(n)
# Space: O(1)
# Status: solved in 1 min / no hint needed / read the editorial

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums), +1):
            nums[i] = nums[i] + nums[i-1]
        return nums