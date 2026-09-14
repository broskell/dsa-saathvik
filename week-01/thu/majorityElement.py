# LC 169 - Majority Element
# https://leetcode.com/problems/majority-element/
# Approach: Boyer-Moore Voting Algorithm maintaining a candidate element and count variable.
# Time: O(n)
# Space: O(1)
# Status: solved in 10 min / no hint needed / read the editorial

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate
