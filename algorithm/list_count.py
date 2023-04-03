# 중복된 숫자 갯수
arr = [1, 1, 1, 2, 3, 4, 5]
n = 1


# 1. 반복문
def solution(arr, n):
    count = 0
    for i in arr:
        if i == n:
            count += 1
    return count


print(solution(arr, n))


# 2. sum(iterable)
def solution2(arr, n):
    return sum(1 for i in arr if i == n)


print(solution2(arr, n))


# 3. list.count()
def solution3(arr, n):
    return arr.count(n)


print(solution3(arr, n))
