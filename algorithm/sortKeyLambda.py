# 가까운 수 구하기. 차가 같을 때는 작은 수를 선택
arr = [10, 11, 12]
n = 13


# 1. elif를 통한 연속적인 비교문 처리
def solution(arr, n):
    arr.append(n)
    arr.sort()
    i = arr.index(n)

    # n의 위치가 양 끝일 경우
    if i == len(arr) - 1:
        return arr[i - 1]
    elif i == 0:
        return arr[1]
    # n의 위치가 중간일 경우
    elif arr[i + 1] - arr[i] < arr[i] - arr[i - 1]:
        return arr[i + 1]
    elif arr[i + 1] - arr[i] >= arr[i] - arr[i - 1]:
        return arr[i - 1]


print(solution(arr, n))


# 2. list.sorted(key=lambda 인자 : 표현식)
def solution2(arr, n):
    arr.sort(key=lambda x: (abs(n - x), x))  #sort는 원본을 변형
    return arr[0]


print(solution2(arr, n))


# 3. min()
def solution3(arr, n):
    arr.sort()
    temp = []
    for i in arr:
        temp.append(abs(i - n))
    return arr[temp.index(min(temp))]


print(solution3(arr, n))


# 4. dict.item()
def solution4(arr, n):
    dict = {i: abs(i - n) for i in arr}
    # sorted(list, key)는 정렬된 것을 반환
    return sorted(dict.items(), key=lambda x: (x[1], x[0]))[0][0]


print(solution4(arr, n))
