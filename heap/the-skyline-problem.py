import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        answers = [[-1, 0]]
        possible_key_pos = sorted(list(set([b[0] for b in buildings] + [b[1] for b in buildings])))
        cur_buildings = []
        idx = 0
        for pos in possible_key_pos:
            while idx < len(buildings) and buildings[idx][0] <= pos:
                heapq.heappush(cur_buildings, (-buildings[idx][2], buildings[idx][1]))
                idx +=1 

            while cur_buildings and cur_buildings[0][1] <= pos:
                heapq.heappop(cur_buildings)
            
            cur_height = -1 * cur_buildings[0][0] if cur_buildings else 0
            if cur_height != answers[-1][1]:
                answers.append([pos, cur_height])
        return answers[1:]
