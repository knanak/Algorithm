# '''
# n과 m
# '''
# from sys import stdin

# n, m = 4,2
# #1. 순열
# from itertools import permutations

# p=list(permutations([i for i in range(1, n+1)], m))
# print(p)

# for i in range(1, m+1):
#   for j in range(1, n+1):
#     if i!=j:
#       print(i ,j)

# #2. 백트래킹 : 재귀함수를 돌며, m개를 선택
# result=[]
# v=[0]*(n+1)
# def recur(num):
#   if num==m:      # 재귀함수를 종료하는 조건
#     print(' '.join(map(str, result)))
#     return

#   for i in range(1, n+1):
#     if v[i]==0:
#       v[i]=1
#       result.append(i)
#       recur(num+1)

#       v[i]=0
#       result.pop()

# recur(0)

N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M: # 배열의 길이를 확인
        print(" ".join(map(str, ans))) # 1 2 3 이런 상태로 출력하기 위해
        return 
    for i in range(1, N+1): # 1 ~ N 까지
        if i not in ans: # 중복 확인
            ans.append(i) # 배열 추가
            back() # 재귀
            print('종료')
            ans.pop() # return으로 돌아오면 이게 실행됨. 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것
            
            
back()