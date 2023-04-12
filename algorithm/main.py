# 분수의 덧셈 : 약분은 최대공약수로
numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4
# 답 : [5, 4]

# 1. math.gcd(a,b)
import math


def solution(numer1, denom1, numer2, denom2):
    n3 = numer1 * denom2 + denom1 * numer2
    d3 = denom1 * denom2

    nn3 = n3 // math.gcd(n3, d3)
    dd3 = d3 // math.gcd(n3, d3)
    return [nn3, dd3]


print(solution(numer1, denom1, numer2, denom2))


# 2. range(시작, 끝, 간격) : 특히 간격이 -인 경우, 거꾸로를 의미
def gcd1(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def solution2(numer1, denom1, numer2, denom2):
    n3 = numer1 * denom2 + denom1 * numer2
    d3 = denom1 * denom2

    gcd = gcd1(n3, d3)
    nn3 = n3 // gcd
    dd3 = d3 // gcd

    return [nn3, dd3]


print(solution2(numer1, denom1, numer2, denom2))

### 최소공배수
a, b = 15, 10

# 1. math.lcm(a,b)은 파이썬 3.9 이상의 버젼부터 사용가능


# 2. range()
def lcm(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


print(lcm(a, b))

### n의 약수
n = 15

# 1. 나머지가 0
result = []
for i in range(1, n + 1):
    if n % i == 0:
        result.append(i)
print(result)

# 2. 약수는 "짝"의 구조로 이뤄졌있다는 컨셉을 이용

## k^2 = n인 경우, k가 중간지점이 되므로, range에도 동일한 구조를 적용
result2 = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        result2.append(i)
        if n // i != i:
            result2.append(n // i)

print(sorted(result2))
