# 주식가격 : 가격이 떨어지지 않는 동안의 기간 출력
prices = [1, 2, 3, 2, 3]  ## 정답 : [4, 3, 1, 1, 0]
# 1. deque
from collections import deque


def solution(prices):
    q = deque(prices)
    result = []
    while q:  ## while반복문과 for i in q 반복문으로 o(n^2)
        sec = 0
        price = q.popleft()
        ## q가 비어있는 경우, 반복문 자체가 실행되지 않아 바로result.append(sec)가 실행됨
        for i in q:
            if price <= i:
                sec += 1
            else:
                sec += 1
                break

        result.append(sec)
    return result


print(solution(prices))

# 2. stack과 -1


# 3. 반복문
def solution3(p):
    ## 리스트 인덱싱을 통해 값을 누적시킬 수 : 조건에 해당하는 갯수 구하기
    result = [0] * len(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] <= p[j]:
                result[i] += 1
            else:
                result[i] += 1
                break
    return result


print(solution3(prices))
