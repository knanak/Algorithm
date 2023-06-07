'''
차이를 최대로
'''

# n=int(input())
# nList=list(map(int, input().split())) 
# result=[]  ## ## nList의 요소가 들어옴
# sum_max=[]

# def back(st): ## 인자로는 인덱스가 들어옴
#   if len(result)==n:
#     global sum_max
#     summ=0
#     for i in range(len(result)-1):
#       summ+=abs(result[i]-result[i+1])
      
#     sum_max.append(summ)
#     return

#   for i in range(st, n):
#     if i not in result:
#       result.append(nList[i])
#       back(i+1)
#       result.pop()
#       print(result)

# back(0)
# print(max(sum_max))

import sys
#sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
visited = [False] *n
tmp = []
ans = []

def dfs(depth):
  global tmp
  
  if len(tmp) == n:
    global ans
    sum = 0
    for i in range(len(tmp)-1):
      sum += abs(tmp[i]-tmp[i+1])
    
    ans.append(sum)
    return
  
  for i in range(st, n+1):
    if not visited[i]:
      visited[i] = True
      tmp.append(numbers[i])
      dfs(depth+1)
      tmp.pop()
      visited[i] = False


dfs(0)
print(max(ans))