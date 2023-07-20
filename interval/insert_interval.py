# link: https://leetcode.com/problems/insert-interval/
# without additional space

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_s, new_e = newInterval
        left_idx = -1
        right_idx = -1
        for idx, (s, e) in enumerate(intervals):
            if e < new_s:
                left_idx = idx
            elif new_e < s:
                if right_idx == -1:
                    right_idx = idx
            else:
                new_s, new_e = min(new_s, s), max(new_e, e)
        left = intervals[:left_idx + 1] if left_idx != -1 else []
        right = intervals[right_idx:] if right_idx != -1 else []
        return left + [[new_s, new_e]] + right
