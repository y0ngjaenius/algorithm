# link: https://leetcode.com/problems/maximum-running-time-of-n-computers

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries = sorted(batteries)
        _sum = sum(batteries)
        while batteries[-1] >  _sum/ n:
            n -= 1
            _sum -= batteries.pop()
        return sum(batteries) // n
