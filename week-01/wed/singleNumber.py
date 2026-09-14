# LC 136 - Single Number
# https://leetcode.com/problems/single-number/
# Approach: Bitwise XOR all numbers. Duplicates cancel out (a ^ a = 0), leaving only the single number.
# Time: O(n)
# Space: O(1)
# Status: solved in 5 min / no hint needed / read the editorial

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
