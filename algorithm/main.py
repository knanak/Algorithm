# how to change character
h = 'happy birth day'
print(h[:4] + h[5:])


# 프로그래머스 더 맵게 문제
# 1. sort() : o(n logn)으로 인해 시간초과
def solution(s, k):
    s.sort()
    cnt = 0

    while s[0] < k:
        new = s.pop(0) + s.pop(0) * 2
        s.append(new)
        s.sort()
        cnt += 1
        if len(s) == 1 and s[0] < k:
            return -1
    return cnt


# 1. heapq : o(logn)으로 성공
import heapq


def solution2(s, k):
    heap = []
    for i in s:
        heapq.heappush(heap, i)
    cnt = 0
    while heap[0] < k:
        new = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, new)
        cnt += 1
        if len(heap) == 1 and heap[0] < k:
            return -1
    return cnt


s = [1, 3, 4, 6]
print(solution(s, 7))
print(solution2(s, 7))
