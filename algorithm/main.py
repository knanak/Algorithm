# 팩토리얼 : i! <= n일때, i의 최대값 구하기
n = 3628800


# 1. 반복문으로 곱해주기
def solution(n):
    answer = 1
    for i in range(2, 11):
        answer *= i  # answer < n이면, 계속 곱해주기
        if answer > n:
            return i - 1
        elif answer == n:
            return i


print(solution(n))

# 2. 끝부터 빼주는 방식
from math import factorial


def solution2(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k  ## factorial(k) >= n이 될때 while문을 빠져나옴


print(solution2(n))


# 3. 재귀함수
def fact(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def solution3(n):
    k = 10
    while n < fact(k):
        k -= 1
    return k  ## factorial(k) >= n이 될때 while문을 빠져나옴


print(solution3(n))


# 4. while과 +=으로 for 반복문 대신하기
def solution4(n):
    answer = 1
    fact = 1
    while fact <= n:
        answer += 1
        fact = fact * answer
    answer = answer - 1
    return answer


print(solution4(n))
