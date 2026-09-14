# LC 88 - Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Approach: Three pointers (p1=m-1, p2=n-1, p=m+n-1) merging elements from back of nums1 to avoid overwriting.
# Time: O(m + n)
# Space: O(1)
# Status: solved in 12 min / no hint needed / read the editorial

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1 