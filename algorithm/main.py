'''
게임맵 최단거리
'''


def solution_bfs(maps):
    from collections import deque
    n, m = len(maps), len(maps[0])
    # (n-1, m-1)에 도달하지 못하는 경우, -1출력해야 하므로, 기본값을 -1로 설정
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visiting = deque([(0, 0)])
    visited[0][0] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    while visiting:
        x, y = visiting.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1 and visited[
                    xx][yy] == -1:
                visited[xx][yy] = visited[x][y] + 1
                visiting.append((xx, yy))
    return visited[n - 1][m - 1]
