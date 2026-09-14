# LC 1929 - Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/
# Approach: Return concatenated array nums + nums.
# Time: O(n)
# Space: O(n)
# Status: solved in 1 min / no hint needed / read the editorial

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums
