# 이진탐색 : 이미 정렬된 리스트에서 시작점, 중간점, 끝점을 이용해 탐색범위를 줄여나가면서 target 데이터를 찾아나감 - 재귀함수 적용 (퀵정렬과 유사). o(logN)

# 이진탐색이 적합한 경우
# ⓐ탐색범위가 클 때, ⓑ조건을 만족하는 경우, 범위를 줄일 수 있을 때

# 1) 값이 특정범위에 속하는 데이터의 갯수 구하기
from bisect import bisect_left, bisect_right

a = [1, 1, 1, 2, 3, 4, 4, 5]

# def count(a, rightVal, leftVal):
#     rightIndex = bisect_right(a, rightVal)
#     leftIndex = bisect_left(a, leftVal)
#     return rightIndex - leftIndex

# print(count(a, 2, 2))

n, x = map(int, input().split())
list = list(map(int, input().split()))


def count1(list, rVal, lVal):
    rIndex = bisect_right(list, rVal)
    lIndex = bisect_left(list, lVal)
    cnt = rIndex - lIndex
    if cnt > 0:
        return cnt
    else:
        return -1


print(count1(list, x, x))

# 2) parametic search : 특정 조건으로 최적화할 수 있나? -> yes/no. yes인 경우 재귀함수으로 반복하여 답을 찾아감
# 떡볶이 떡 만들기 문제 : 적어도 m만큼의 떡을 가져가기 위한 최대 h의 높이

# n, m = map(int, input().split())
# list = list(map(int, input().split()))
# n, m = 4, 6
# list = [19, 15, 17, 10]

# def cut(list, m, start, end):
#     result = 0
#     mid = (start + end) // 2
#     if start > end:
#         return mid

#     for i in list:
#         if (i - mid) > 0:
#             result += (i - mid)
#             if result > m:
#                 cut(list, m, start + 1, end)
#             else:
#                 cut(list, m, start, end - 1)

# print(cut(list, m, 0, max(list)))
