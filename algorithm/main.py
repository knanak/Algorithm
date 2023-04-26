'''
구명보트를 최소한으로 이용하기 위해서는 최대+최소 값을 기준으로 찾아야 한다.
'''
people = [70, 80, 50]
limit = 100
# 답 :3

# 1. deque
from collections import deque


def solution(p, limit):
    p = deque(sorted(p))
    boat = 0

    while len(p) >= 2:  # 보트에 최소 2명이 남은 경우까지 반복

        if p[0] + p[-1] <= limit:
            boat += 1
            p.pop()
            p.popleft()
        else:
            boat += 1
            p.pop()

    if p:  # 보트에 1명이 남는 경우
        boat += 1

    return boat


print(solution(people, limit))


# 2. 투 포인터
def solution2(people, limit):
    people.sort()
    cnt = 0
    left, right = 0, len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            cnt += 1
        right -= 1
    return len(people) - cnt


print(solution2(people, limit))
