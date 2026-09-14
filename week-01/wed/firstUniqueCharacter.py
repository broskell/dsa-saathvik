# LC 387 - First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Approach: Two passes - count frequencies with Counter, then scan string for first char with count 1.
# Time: O(n)
# Space: O(1) - fixed alphabet size of 26 letters
# Status: solved in 8 min / no hint needed / read the editorial

from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        return -1
