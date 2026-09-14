# LC 242 - Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Approach: Compare character frequency counts of both strings using Counter.
# Time: O(n)
# Space: O(1) - fixed alphabet size of 26 lower-case English characters
# Status: solved in 5 min / no hint needed / read the editorial

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        anagramMap = {}

        for letter in s:
            anagramMap[letter] = anagramMap.get(letter, 0) + 1
            
        for letter in t:
            if letter not in anagramMap:
                return False
            anagramMap[letter] -= 1
        
        for count in anagramMap.values():
            if count != 0:
                return False
           
        return True