# LC 268 - Missing Number
# https://leetcode.com/problems/missing-number/
# Approach: Compute expected sum n*(n+1)//2 and subtract total sum of nums array.
# Time: O(n)
# Space: O(1)
# Status: solved in 5 min / no hint needed / read the editorial

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
