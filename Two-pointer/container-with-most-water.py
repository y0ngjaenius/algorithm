# link: https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, e = 0, len(height) - 1
        max_water = min(height[s], height[e]) * (e - s)
        while s < e:
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
            max_water = max(max_water, min(height[s], height[e]) * (e - s))
        return max_water
