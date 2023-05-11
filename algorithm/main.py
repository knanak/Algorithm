'''타겟넘버 : numbers로 target을 만들 수 있는 경우의 수'''

# 1. bfs : 형제노드부터 방문
from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])

    while q:
        result, idx = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append([result + numbers[idx], idx])
            q.append([result - numbers[idx], idx])

        elif idx == len(numbers):
            if result == target:
                answer += 1

    return answer


print(solution([4, 1, 2, 1], 4))

# 2. dfs : 자식노드의 끝까지 먼저 방문
answer = 0


def dfs(numbers, target, idx, result):
    global answer
    if idx == len(numbers) and result == target:
        answer += 1
        return
    elif idx == len(numbers):
        return

    dfs(numbers, target, idx + 1, result + numbers[idx])
    dfs(numbers, target, idx + 1, result - numbers[idx])


def solution2(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer


print(solution2([4, 1, 2, 1], 4))
