# LC 217 - Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Approach: Use a hash set to track seen elements in O(1) lookup time per element.
# Time: O(n)
# Space: O(n)
# Status: solved in 5 min / no hint needed / read the editorial

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
