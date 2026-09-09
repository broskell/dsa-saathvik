# LC 1470 — Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/
# Time: O(n)
# Space: O(n)
# Status: solved in 5 min / no hint needed / read the editorial

# Brute force approach
class Solution(object):
    def shuffle(self, nums, n):
        output = [0] * (2 * n)
        
        for i in range(0, len(nums) // 2, +1):
            output[i * 2] = nums[i]
        insert = 1
        for j in range(len(nums) // 2, len(nums), +1):
            output[insert] = nums[j]
            insert += 2
        return output

# Optimized approach
class Solution(object):
    def shuffle(self, nums, n):
        output = []

        for i in range(0, n, +1):
            output.append(nums[i])
            output.append(nums[i + n])
        return output