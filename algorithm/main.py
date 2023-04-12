# 연속된 num의 합 = total
num = 5
total = 5

# 정답 : [-1, 0, 1, 2, 3]


# 1. 중간값 이용 : 식 세우기, num//2를 통해 양쪽에 몇 개 있는지 알 수
def solution(num, total):
    if num % 2 == 1:
        mid = total // num
        return [i for i in range(mid - num // 2, mid + num // 2 + 1)]

    else:
        mid = total // num + 1
        return [i for i in range(mid - num // 2, mid + num // 2)]


print(solution(num, total))


# 2. while, i+=1
def solution2(num, total):
    li = [i for i in range(-num - total, num + total + 1)]
    i = 0
    while sum(li[i:i + num]) != total:
        i += 1
    return li[i:i + num]


print(solution2(num, total))


# 3. for 반복문
def solution3(num, total):
    li = [i for i in range(-num - total, num + total + 1)]
    for i in range(len(li)):
        if sum(li[i:i + num]) == total:
            return li[i:i + num]


print(solution3(num, total))
