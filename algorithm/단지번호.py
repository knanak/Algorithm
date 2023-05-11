'''
단지번호 붙이기 : 단지의 총 갯수와 각 단지에는 아파트가 몇개가 있는지
'''

from sys import stdin

# n = int(input())
# x = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
# v = [[False] * n for _ in range(n)]

# 1. bfs : 큐
from collections import deque

n = int(input())
graph = [list(map(int, stdin.readline().rstrip())) for i in range(n)]
visited = [[False] * n for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
cnt = 0


def bfs(xPos, yPos):
    count = 1
    q = deque()
    q.append((xPos, yPos))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    ans.append(count)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            bfs(i, j)

ans.sort()

print(len(ans))
for i in ans:
    print(i)

# 2. dfs : 재귀함수, 스택
# each = 0
# result = []

# dy = [1, 0, -1, -0]
# dx = [0, 1, 0, -1]
# print(x[0][1])
# print(v[0][1])

# def dfs(y, x):
#     global each
#     each += 1
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if x[ny][nx] == 1 and v[ny][nx] == False:
#                 v[ny][nx] == True
#                 dfs(ny, nx)

# for j in range(n):
#     for i in range(n):
#         if x[j][i] == 1 and v[j][i] == False:
#             v[j][i] = True
#             each = 0
#             dfs(j, i)  # -> each(1로 연결된 갯수)가 나오게됨
#             result.append(each)

# result.sort()
# print(len(result))
# for i in result:
#     print(i)
