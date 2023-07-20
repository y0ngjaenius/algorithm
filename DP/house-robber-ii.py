# link: https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            rob_last, not_rob_last = 0, 0
            for num in nums:
                rob_last, not_rob_last = not_rob_last + num, max(rob_last, not_rob_last)
            return max(rob_last, not_rob_last)
        N = len(nums)
        if N == 1:
            return nums[0]
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))
