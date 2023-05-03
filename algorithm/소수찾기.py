'''
소수의 연속합이 n이 되는 경우의 수
'''

n = int(input())

# 1-1. n까지의 소수 찾기 : 반복문 o(n**0.5)
# def is_prime(num):
#     for i in range(2, int(num**(1 / 2)) + 1):
#         if num % i == 0:
#             return False
#     return True

# primes = []
# for i in range(2, n + 1):
#     if is_prime(i) == True:
#         primes.append(i)

# print(primes)

# 1-2. 에라토스테네스의 체 : 소수의 배수 지우기
arr = [True for i in range(n + 1)]
for i in range(2, int(n**0.5) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

primes=[]
for i in range(2, n + 1):
    if arr[i]: 
      primes.append(i)

# 2. 소수의 연속합이 n의 되는 경우의 수
# st, end = 0, 1
# result = primes[0]
# cnt = 0

# while True:
#     if result < n:
#         if end < len(primes):
#           result += primes[end]
#           end += 1

#         else:
#             break

#     elif result == n:
#         cnt += 1
#         result -= primes[st]
#         st += 1

#     else:
#         result -= primes[st]
#         st += 1

# print(cnt)
