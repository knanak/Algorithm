'공넣기'

# for i in mList:
#   # 리스트의 범위 할당시, 리스트로 넣어줘야
#   b[i[0]:i[1]+1]=[i[2] for _ in range(i[1]-i[0]+1)]


# print(' '.join(map(str, b[1:])))


# 2. input()의 반복문으로 i,j,k 받아오기
# N, M = map(int, input().split())
# basket = [0 for _ in range(N+1)]

# # 반복문으로 i,j,k 받아오기
# for _ in range(M):
#     i,j,k = map(int, input().split())
#     for n in range(i,j+1):
#         basket[n] = k

# for n in range(1, N+1):
      # print( end='') 옵션을 통해 줄바꿈 대신 원하는 구분자를 넣을 수 있다
#     print(basket[n], end = ' ')

'''
공 바꾸기 : 2개의 바구니를 선택하고, m번 공을 바꿈
'''
# n,m=map(int, input().split())
# b=[i for i in range(n+1)]
# for _ in range(m):
#   i, j = map(int, input().split())
#   b[i], b[j] = b[j], b[i]

# for i in range(1, n+1):
#   print(b[i], end=' ')

'''
공 : m번 바꾼 후, 공이 들어있는 컵의 번호
'''
m=int(input())
b=[0,1,0,0]
for _ in range(m):
  x,y=map(int, input().split())
  b[x], b[y]= b[y], b[x]

print(b.index(1))