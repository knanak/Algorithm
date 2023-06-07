'''
공넣기 : 바구니의 범위를 정하고, 같은 번호의 공을 m번 넣기
'''

n,m=map(int, input().split())
mList=[list(map(int, input().split())) for _ in range(m)]
b=[0 for _ in range(n+1)]

for i in mList:
  # 리스트의 범위 할당시, 리스트로 넣어줘야
  b[i[0]:i[1]+1]=[i[2] for _ in range(i[1]-i[0]+1)]


print(' '.join(map(str, b[1:])))


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