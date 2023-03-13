#4) counting sort : o(데이터갯수+j), 점수가 동일한 경우 등 카운팅할때 사용하고, 요소들의 간격이 너무 큰 경우는 비효율적 cf. 원핫인코딩
data = list(map(int, input()))
list = [0] * (max(data) + 1)

for i in data:
    list[i] += 1

# for i in data:
# str으로 받아 반복문 처리 한후에는 비교 위해 int로 변경
#     i = int(i)
#     for j in range(len(list)):
#         if i == j:
#             list[j] += 1  # 조건만족 시 +1하면서 counting

for idx, i in enumerate(list):
    for j in range(i):
        print(idx, end=' ')
