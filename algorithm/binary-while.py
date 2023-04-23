'''
이진탐색은 
1. "찾는 값"이 무엇인지를 파악해 return 값으로 설정하고, 이를 기준으로 start, end, mid를 설정한다. 
2. 찾는 값이 명확한 경우, 재귀함수를 통해 찾고, 
  찾는 값이 명확하지 않은 경우(trial and error 하면서 찾아야 하는 경우),    while 반복문을 통해 찾는다.

이진탐색의 조건
1. 정렬
2. start, end 설정 -> mid
3. 재귀 or while : 찾는 값이 명확하냐 or 명확x
4. 종료조건 : st=end or st<=end 동안에는 반복하고, 그외에는 반복문 탈출
'''
'''
입국심사 시 걸리는 시간이 최소가 되도록
'''

n = 6
times = [7, 10]
## 정답 : 28


def solution(n, times):
    st, end = 1, max(times) * n
    res = end  # 총 심사시 걸리는 최소 시간

    while st <= end:
        mid = (st + end) // 2
        people = 0

        for t in times:  # 면접관마다 심사시 걸리는 시간
            people += mid // t  # 총시간//면접관 당 시간

        if people < n:
            st = mid + 1
        else:
            end = mid - 1
            res = min(res, mid)

    return res


print(solution(n, times))
