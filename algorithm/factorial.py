# 팩토리얼 : 1부터 n까지의 곱

# 함수 범위 주의
# result=1로 함수 밖에서 할당 할 경우, 함수 안에서 할당 전 사용 오류가 남

# def f(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#         # return값이 for 반복문 안에 있는 경우, 첫번째 반복문을 끝내면 return하기 때문에 설정된 range만큼 반복되지 못한채 종료됨
#         # return result

#     return result

# print(f(5))

# # 2) 재귀함수로 구현

# def f_self(n):
#     if n <= 1:
#         return 1
#     return n * f_self(n - 1)

# print(f_self(5))

# 3) 재귀함수를 이용한 최대 공약수 구하기 : 유클리드 호제법
# 두 자연수 A,B(A<B)가 있고, A로 B를 나눈 나머지가 R일때, A와 B의 최대공약수는 B와 R의 최대 공약수와 같다


def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    return gcd(y, r)


print(gcd(100, 30))
