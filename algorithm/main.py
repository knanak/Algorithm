# 연속으로 중복된 숫자 제거하기
arr = [1, 1, 3, 3, 0, 1, 1]  # 답 : [1,3,0,1]


# 1. stack 이용
def solution(arr):
    result = []
    for i in arr:
        if result[-1:] != [i]:
            result.append(i)
    return result


print(solution(arr))


# 1-1. continue 이용 : 조건에 해당하는 경우, 건너뛰기
def solution2(arr):
    result = []
    for i in arr:
        if result[-1:] == [i]:
            continue
        result.append(i)
    return result


print(solution2(arr))

## 답은 맞았지만, 시간초과된 문제들 : 배열 arr의 크기 : 최대 10^6 까지 될 수므로, 시간복잡도가 n^2인 경우 시간초과됨. 따라서 전체를 비교하는 풀이가 아닌, 스택구조를 사용한 맨 마지막 값만을 비교해여 풀어야 함


# 2. if not in 으로 비교
def solution3(arr):
    k = []
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:  # 반복문, if문 비교자체로 n(n^2)
            k.append(i)

    m = []
    for i in range(len(arr)):
        if i not in k:
            m.append(arr[i])
    return m


print(solution3(arr))


# 2-1. stack.pop()으로 중복값 빼주기
def solution4(arr):
    k = []
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:  # 반복문, if문 비교자체로 n(n^2)
            k.append(i)

    while k:
        arr.pop(k[-1])
        k.pop(-1)

    return arr


print(solution4(arr))
