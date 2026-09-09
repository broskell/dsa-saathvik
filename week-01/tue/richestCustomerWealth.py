# LC 1672 — Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/
# Time: O(n)
# Space: O(1)
# Status: solved in 1 min / no hint needed / read the editorial

class Solution(object):
    def maximumWealth(self, accounts):
        maxi = 0
        for acc in accounts:
            maxi = max(maxi, sum(acc))
        return maxi