# 머쓱이보다 키 큰 사람의 수
arr = [180, 120, 140]
h = 190

# 답 : 0


# 1. list.sort(reverse=True) 후, 인덱스로 갯수 세기
def solution(arr, h):
    arr.append(h)
    arr.sort(reverse=True)
    return arr.index(h)


print(solution(arr, h))


# 2. sum(list)
def solution2(arr, h):
    return sum([1 for i in arr if i > h])


print(solution2(arr, h))
