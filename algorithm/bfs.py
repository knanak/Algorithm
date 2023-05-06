from sys import stdin

n, m = map(int, stdin.readline().split())
map = [list(map(int, stdin.readline().split())) for _ in range(n)]

visit = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    result = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and visit[ny][nx] == False:
                    result += 1
                    visit[ny][nx] = True
                    q.append((ny, nx))  #새로 방문한 노드를 추가

    return result


cnt, maxv = 0, 0  # 그림의 갯수, 그림의 넓이
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and visit[j][i] == False:
            visit[j][i] = True
            cnt += 1
            #그림의 넓이인 result를 bfs()와 비교하며 최대값으로 갱신
            # bfs()를 통과하면서 연결된 값들은 True 처리가 됨
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)
