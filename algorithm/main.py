# 배포순서와 개발속도를 고려하여 배포되는 숫자 구하기
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]  # 정답 : [1, 3, 2]

## (1) 현재까지 진행률과 개발속도를 고려해서 배포까지 남은 날짜 구하기

## (2) 남은 날짜와 배포순서를 고려하여 배포하기. 배포순서를 고려하여 앞에서부터 처리되야 하기 때문에 que 자료구조를 사용하거나, list.pop(0)을 사용함

# 1. math.ceil() 사용하여 남은 날짜 구하고, que 자료구조를 사용해 비교하기
import queue
import math


def solution(progresses, speeds):
    q = queue.Queue()
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        q.put(day)

    first = q.get()
    result = [1]
    for i in range(1, len(progresses)):
        next = q.get()
        if first >= next:
            result[-1] += 1
        else:
            result.append(1)
            first = next
    return result


print(solution(progresses, speeds))


# 2. 인덱스와 뺄셈을 사용해서 몇개가 남았는지 구하기
def solution2(progresses, speeds):
    result = []
    for i in range(len(progresses)):
        result.append(math.ceil((100 - progresses[i]) / speeds[i]))

    now = 0
    answer = []
    for i in range(1, len(progresses)):
        if result[now] < result[i]:  # 현재보다 더 큰 수를 만나면, 배포
            answer.append(i - now)
            now = i
    # 반복문 조건을 탈출한 경우(현재보다 작은수만 있을 때), now에서의 마지막 배포
    answer.append(len(progresses) - now)
    return answer


print(solution2(progresses, speeds))
