# link: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

import math

class Solution:
    def ispossible(self, dist: List[int], hour: float, speed: int) -> bool:
        return sum([math.ceil(dis / speed) for dis in dist[:-1]]) + dist[-1] / speed <= hour

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
        start = 1
        end = 10 ** 7
        
        while start <= end:
            mid = start + (end - start) // 2
            if self.ispossible(dist, hour, mid):
                end = mid - 1
            else:
                start = mid + 1

        return start
