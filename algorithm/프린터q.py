'''
프린터 q : 중요도 비교하여 출력. 중요도가 낮으면 맨뒤로 보냄
'''

# from collections import deque
# case=int(input())


# for _ in range(case):
#   n,m=map(int, input().split())
#   v=list(map(int, input().split()))
#   q=deque(v)
#   idx=m
#   for i in range(n):
#     if q[0] == max(q):
#       continue
#     else :
      
#       q.popleft()
#       q.append(q[i])
#       idx=m-1

#   print(idx)

a=list(range(4))
print(a)