'''
동일한 숫자카드를 몇 개 가지고 있는가
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

정답 : 3 0 0 1 2 0 0 2
'''

from sys import stdin

_ = stdin.readline()
n = list(map(int, stdin.readline().split()))
_ = stdin.readline()
m = list(map(int, stdin.readline().split()))

# 1. counter(list)
from collections import Counter

c = Counter(n)

result = []
for i in m:
    if i in c:
        result.append(c[i])
    else:
        result.append(0)

print(' '.join(map(str, result)))

# 2. dict
dic = {}
for i in n:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

result2 = []
for i in m:
    if i in dic:
        result2.append(dic[i])
    else:
        result2.append(0)

print(' '.join(map(str, result2)))
