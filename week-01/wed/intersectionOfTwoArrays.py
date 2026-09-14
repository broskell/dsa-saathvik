# LC 349 - Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# Approach: Convert both lists to hash sets and compute set intersection for O(n + m) time.
# Time: O(n + m)
# Space: O(n + m)
# Status: solved in 5 min / no hint needed / read the editorial

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
