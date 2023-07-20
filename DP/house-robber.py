# link: https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_last, not_rob_last = 0, 0
        for num in nums:
            rob_last, not_rob_last = not_rob_last + num, max(rob_last, not_rob_last)
        return max(rob_last, not_rob_last)
