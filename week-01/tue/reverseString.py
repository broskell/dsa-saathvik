# LC 344 - Reverse String
# https://leetcode.com/problems/reverse-string/
# Time: O(n)
# Space: O(1)
# Status: solved in 1 min / no hint needed / read the editorial

class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1