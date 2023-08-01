# link: https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        answer = set()
        one_dic = {num: idx for idx, num in enumerate(nums)}
        two_sum_dic = {}
        for idx, num in enumerate(nums):
            if not two_sum_dic:
                two_sum_dic[num] = idx
                continue
            for other_num in two_sum_dic:
                if -1 * (num + other_num) in one_dic:
                    if len(set([idx, two_sum_dic[other_num], one_dic[-1 * (num + other_num)]])) == 3:
                        answer.add(tuple(sorted([num, other_num, -1 * (num + other_num)])))
            two_sum_dic[num] = idx
        return [list(tup) for tup in answer]
