# LC 238 - Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Approach: Two passes: left prefix product pass populating output array, right suffix product pass accumulating in scalar.
# Time: O(n)
# Space: O(1) auxiliary space (excluding returned result array)
# Status: solved in 25 min / no hint needed / read the editorial

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        prefix, suffix = 1, 1

        for i in range(0, len(nums), +1):
            answer[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer