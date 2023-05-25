'''
가장 먼 노드 : 단순히 방문처리로 하는게 아니라, 몇번 방문했는지 기록하기 위해서는 몇 번 노드가 몇 번 노드에 방문했는지 나타내는 그래프가 필요
'''

n=6	
edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import deque
def solution(n, edge):
  graph=[[] for i in range(n+1)]
  v=[0]*(n+1) ## 몇 번 방문했는지 체크

  for ed in edge:
    x,y=ed[0], ed[1]
    graph[x].append(y)
    graph[y].append(x)

  q=deque()
  q.append(1)
  v[1]=1

  while q:
    x=q.popleft()
    for i in graph[x]:
      if not v[i] : ## v가 0인지 체크
        v[i]=v[x]+1
        q.append(i)

  maxVal=max(v)
  answer=v.count(maxVal)
  return answer

print(solution(n, edge))