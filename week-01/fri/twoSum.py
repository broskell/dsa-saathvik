# LC 1 - Two Sum
# https://leetcode.com/problems/two-sum/
# Approach: One-pass hash map storing value -> index; look up complement.
# Time: O(n)
# Space: O(n)
# Status: solved in 5 min / no hint needed / read the editorial

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
