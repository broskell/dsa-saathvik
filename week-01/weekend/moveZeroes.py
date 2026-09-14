# LC 283 - Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Approach: Two pointers (write_ptr and i). Swap non-zero elements to write_ptr position in-place.
# Time: O(n)
# Space: O(1)
# Status: solved in 8 min / no hint needed / read the editorial

class Solution(object):
    def moveZeroes(self, nums):
        insertPos = 0

        for i in range(0, len(nums), +1):
            if nums[i] != 0:
                nums[insertPos], nums[i] = nums[i], nums[insertPos] 
                insertPos += 1         
        return nums