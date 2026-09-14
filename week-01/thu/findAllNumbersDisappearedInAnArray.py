# LC 448 - Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-array/
# Approach: In-place index marking. Mark nums[abs(val) - 1] as negative. Unmarked positive values indicate missing numbers.
# Time: O(n)
# Space: O(1) extra space (excluding output array)
# Status: solved in 12 min / no hint needed / read the editorial

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
                
        return result
