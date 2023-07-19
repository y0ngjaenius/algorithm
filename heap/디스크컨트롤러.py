# link: https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq

def solution(jobs):
    cur_time, total_latency = 0, 0
    heap = []
    N = len(jobs)
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]), reverse=True)
    job = jobs.pop()
    heapq.heappush(heap, (job[1], job[0]))
    while heap:
        duration, arrival = heapq.heappop(heap)
        cur_time = max(duration + arrival, duration + cur_time)
        total_latency += cur_time - arrival
        while jobs and jobs[-1][0] <= cur_time:
            job = jobs.pop()
            heapq.heappush(heap, (job[1], job[0]))
        if jobs and not heap:
            job = jobs.pop()
            heapq.heappush(heap, (job[1], job[0]))
    answer = int(total_latency / N)
    return answer
