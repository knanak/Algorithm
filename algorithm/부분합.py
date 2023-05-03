'''
부분합
'''
from sys import stdin

n, s = map(int, stdin.readline().split())
nList = list(map(int, stdin.readline().split()))

st, end = 0, 1
result = nList[0]

# 1. 값을 비교하기 : 리스트에 넣고, 마지막에 비교
# cnt = []

# while True:
#     if result < s:
#         if end < n:
#             result += nList[end]
#             end += 1
#         else:
#             break

#     else:
#         cnt.append(end - st)
#         result -= nList[st]
#         st += 1

# if cnt:
#     print(min(cnt))
# else:
#     print(0)

# 2. 값을 비교하기2 : 변수에 넣어 과정마다 비교하기
ans = n + 1

# '''
# 수들의 합2 : 연속된 범위의 수의 합이 m이 되는 경우의 수
# '''

# from sys import stdin

# n, m = map(int, stdin.readline().split())
# nList = list(map(int, stdin.readline().split()))

# # 1. 투 포인터 : 포인터가 가르키는 것은 무엇인가
# st, end = 0, 1
# sum = nList[0]
# cnt = 0
# while end <= n - 1:
#     if sum < m:
#         sum += nList[end]
#         end += 1
#     elif sum == m:
#         cnt += 1
#         st += 1
#         sum -= nList[st]
#     else:
#         sum -= nList[st]
#         st += 1
# print(cnt)
