# LC 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Approach: Group words in defaultdict(list) using character frequency tuple (or tuple of sorted chars) as hash key.
# Time: O(n * k) where n is number of strings and k is max length of a string
# Space: O(n * k)
# Status: solved in 15 min / no hint needed / read the editorial

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
