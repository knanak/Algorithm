'''
피로도. 전체 n의 갯수가 많지 않을 경우, 완전 탐색 가능성
'''
k=80	
d=[[80,20],[50,40],[30,10]] # 답 : 3

# 1. 조합 : 순서x
from itertools import permutations
def solution(k,d):
  answer=0
  for pm in permutations(d, len(d)): # pm은 던전가는 순서도
    hp=k    # 반복문으로 새로운 순서도를 탐험할때마다 hp 초기화
    cnt=0

    for p in pm:
      if hp >= p[0]:
        hp-=p[1]
        cnt+=1

    if cnt > answer :
      answer=cnt  

  return answer

print(solution(k,d))

# 2. dfs
answer, n = 0, 0  # global 변수는 재할당할 경우, 스코프 안에서 global 지정해야
v=[]

def dfs(cnt, d, k): # global 변수 외에 필요한 것들 넣어주기
  global answer
  if cnt > answer:
    answer = cnt
    
  for i in range(n):  
    if d[i][0]<=k and not v[i]:
      v[i]=1
      dfs(cnt+1, d, k-d[i][1])
      v[i]=0    # for문으로 새로운 i번쨰 던전에 방문해야하므로, 방문초기화

def solution2(k,d):
  global n, v
  n=len(d)
  v=[0]*n
  dfs(0, d, k)
  return answer

print(solution2(k,d))