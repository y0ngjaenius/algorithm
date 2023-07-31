# link: https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        max_len = 0
        cur_end = -(10 ** 6)
        for s, e in sorted_intervals:
            if cur_end <= s:
                max_len += 1
                cur_end = e
        return len(intervals) - max_len
