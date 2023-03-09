# 방문 노드가 1부터 시작하기 때문에 0번째 인덱스는 비워둠
graph = [[], [2, 3, 8], [
    1,
    7,
], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9

# DFS 알고리즘 : 하나의 방법을 파고드는 경우, 재귀함수나 반복문을 이용


def dfs(v, graph, visited):
    visited[v] = True
    print(v, end='')

    for i in graph[v]:
        if visited[i] == False:
            dfs(i, graph, visited)


dfs(1, graph, visited)

# BFS 알고리즘 : 너비 우선 : 여러 방법을 한번씩 시도해보는 경우, queue, linkedList
from collections import deque


def bfs(start, graph, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        print(v, end='')

        # start는 while 범위 밖에 있기 때문에 반복문 안에 있는 v를 넣어줘야
        # for in graph[start]:
        for i in graph[v]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True


bfs(1, graph, visited)
