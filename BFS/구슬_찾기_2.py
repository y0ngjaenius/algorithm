# link: https://www.acmicpc.net/problem/13460
# 삼성 기출

import sys
from collections import deque

input = sys.stdin.readline
dic_map = {'l': (0, -1),
           'r': (0, 1),
           'u': (-1, 0),
           'd': (1, 0)}

def parse_input():
    N, M = map(int, input().split(" "))
    board = []
    r_start = -1, -1
    b_start = -1, -1
    for X in range(N):
        line = input().strip()
        r_finder = line.find("R")
        if r_finder != -1:
            r_start = (X, r_finder)
            line = line[:r_finder] + "." + line[r_finder + 1:]
        b_finder = line.find("B")
        if b_finder != -1:
            b_start = (X, b_finder)
            line = line[:b_finder] + "." + line[b_finder + 1:]
        board.append(line)
    return N, M, board, r_start, b_start

class Board:
    def __init__(self, r, b, count, direction='l'):
        self.r = r
        self.b = b
        self.count = count
        self.direction = direction
        
    def r_first(self):
        if self.direction == 'l':
            return self.b[1] >= self.r[1]
        elif self.direction == 'r':
            return self.b[1] <= self.r[1]
        elif self.direction == 'u':
            return self.b[0] >= self.r[0]
        else:
            return self.b[0] <= self.r[0]
    
    def go_direction(self):
        dx, dy = dic_map[self.direction]
        r_first = self.r_first()
        completed, pruned = False, False
        first, second = (self.r, self.b) if r_first else (self.b, self.r)
        first_done, second_done = False, False
        while not first_done:
            next_pos = first[0] + dx, first[1] + dy
            if board[next_pos[0]][next_pos[1]] == "#":
                first_done = True
            elif board[next_pos[0]][next_pos[1]] == "O":
                if r_first: # this is R
                    first = -1, -1
                    completed, first_done = True, True
                else:
                    first = -1, -1
                    pruned, first_done = True, True
            else:
                first = next_pos
        while not second_done:
            next_pos = second[0] + dx, second[1] + dy
            if next_pos == first or board[next_pos[0]][next_pos[1]] == "#":
                second_done = True
            elif board[next_pos[0]][next_pos[1]] == "O":
                if r_first: # this is B
                    pruned, second_done = True, True
                else:
                    completed, second_done = True, True
            else:
                second = next_pos
        r, b = (first, second) if r_first else (second, first)
        return r, b, completed, pruned

def solution(N, M, board, r_start, b_start):
    queue = deque([])
    visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[r_start[0]][r_start[1]][b_start[0]][r_start[1]] = True
    for dirc in ['l', 'r', 'u', 'd']:
        queue.append(Board(r_start, b_start, 1, dirc))
    while queue:
        cur_board = queue.popleft()
        if cur_board.count > 10:
            return -1
        r, b, completed, pruned = cur_board.go_direction()
        if completed and not pruned:
            return cur_board.count
        elif pruned:
            continue
        else:
            if not visited[r[0]][r[1]][b[0]][b[1]]:
                visited[r[0]][r[1]][b[0]][b[1]] = True
                for dirc in ['l', 'r', 'u', 'd']:
                    if dirc != cur_board.direction:
                        queue.append(Board(r, b, cur_board.count + 1, dirc))
    return -1
               
N, M, board, r_start, b_start = parse_input()
print(solution(N, M, board, r_start, b_start))
