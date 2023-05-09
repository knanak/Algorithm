from collections import deque

n, k = map(int, input().split())
q = deque([n])
time = [-1] * 100001
time[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(time[s])
        break

    for i in [2 * s, s - 1, s + 1]:
        if 0 <= i < 100001 and time[i] == -1:
            if i == 2 * s:
                time[i] = time[s]
                q.appendleft(i)
            else:
                time[i] = time[s] + 1
                q.append(i)

    # if 0 <= s-1 < 100001 and visited[s-1] == -1:
    #     visited[s-1] = visited[s] + 1
    #     q.append(s-1)

    # if 0 < s*2 < 100001 and visited[s*2] == -1:
    #     visited[s*2] = visited[s]
    #     # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    #     q.appendleft(s*2)

    # if 0 <= s+1 < 100001 and visited[s+1] == -1:
    #     visited[s+1] = visited[s] + 1
    #     q.append(s+1)
