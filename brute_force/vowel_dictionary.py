# link: https://school.programmers.co.kr/learn/courses/30/lessons/84512

alp = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

def solution(word):
    answer = 0
    N = len(word)
    for i in range(N):
        sub = 0
        e = 4 - i
        while e >= 0:
            sub += (5 ** e)
            e -= 1
        answer += (sub * alp[word[i]] + 1)
    return answer
