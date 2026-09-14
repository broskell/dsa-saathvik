# LC 1 - Two Sum
# https://leetcode.com/problems/two-sum/
# Approach: One-pass hash map storing value -> index; look up complement (target - value).
# Time: O(n)
# Space: O(n)
# Status: solved in 10 min / no hint needed / read the editorial

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in seen:
                return [seen[complement], i]
            seen[v] = i
        return []
