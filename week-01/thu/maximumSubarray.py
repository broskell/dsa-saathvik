# LC 53 - Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Approach: Kadane's Algorithm - dynamic programming tracking max subarray sum ending at current position.
# Time: O(n)
# Space: O(1)
# Status: solved in 15 min / no hint needed / read the editorial

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
