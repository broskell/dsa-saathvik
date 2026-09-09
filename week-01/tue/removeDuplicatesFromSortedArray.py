# LC 26 - Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Time: O(n)
# Space: O(1)
# Status: solved in 2 min / no hint needed / read the editorial

class Solution(object):
    def removeDuplicates(self, nums):
        unique = 0

        for j in range(0, len(nums), +1):
            if nums[unique] != nums[j]:
                unique += 1
                nums[unique] = nums[j]
        return unique + 1