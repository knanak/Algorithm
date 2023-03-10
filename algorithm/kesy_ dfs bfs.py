# keys와 rooms 문제

rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
visited = [False] * len(rooms)


# 깊이 탐색
def dfs(v):
    visited[v] = True

    for i in rooms[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

    if False not in visited:
        return True

    else:
        return False


print(dfs(0))

# 너비탐색
from collections import deque

que = deque()


def bfs(v):
    que.append(v)  # bfs만의 특징
    visited[v] = True

    while que:
        n = que.popleft()  # bfs만의 특징
        for i in rooms[n]:  # bfs만의 특징
            if not visited[i]:
                que.append(i)
                visited[i] = True

    if all(visited):
        return True
    else:
        return False


print(bfs(0))
