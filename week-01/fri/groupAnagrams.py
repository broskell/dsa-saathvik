# LC 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Approach: Group strings into defaultdict using a 26-element character count tuple key.
# Time: O(n * k)
# Space: O(n * k)
# Status: solved in 12 min / no hint needed / read the editorial

class Solution(object):
    def groupAnagrams(self, strs):
        strMap = {}

        for string in strs:
            sortedString = ''.join(sorted(string))

            if sortedString not in strMap:
                strMap[sortedString] = []

            strMap[sortedString].append(string)
        return list(strMap.values())