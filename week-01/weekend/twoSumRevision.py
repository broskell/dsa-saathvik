# LC 1 - Two Sum (Spaced Revision)
# https://leetcode.com/problems/two-sum/
# Approach: Timed re-solve from blank file using hash map complement lookup.
# Time: O(n)
# Space: O(n)
# Status: solved in 3 min / no hint needed / read the editorial

class Solution(object):
    def twoSum(self, nums, target):
        output = {}

        for i in range(0, len(nums), +1):
            required = target - nums[i]
            if required in output:
                return i, output[required]
            output[nums[i]] = i