# LC 350 - Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Approach: Count frequencies of smaller array using Counter, match and decrement for elements in second array.
# Time: O(n + m)
# Space: O(min(n, m))
# Status: solved in 10 min / no hint needed / read the editorial

class Solution:
    def intersect(self, nums1, nums2):
        counts = {}
        result = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result