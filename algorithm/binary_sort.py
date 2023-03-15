# 이진탐색 : 이미 정렬된 리스트에서 시작점, 중간점, 끝점을 이용해 탐색범위를 줄여나가면서 target 데이터를 찾아나감 - 재귀함수 적용 (퀵정렬과 유사). o(logN)

list = list(map(int, input()))
target, n = map(int, input().split())


def bSearch(start, end, target, list):
    if end < start:
        return None

    mid = (start + end) // 2

    if list[mid] == target:
        return mid  # target이 몇 번째에 들어있는지 반환

    if list[mid] > target:  #target보다 큰 쪽은 버려 탐색범위 줄이기
        bSearch(start, mid - 1, target, list)

    else:
        bSearch(mid + 1, end, target, list)


result = bSearch(0, n - 1, target, list)

if result == None:
    print('해당 값이 존재하지 않음')
else:
    print(result + 1)  ## 인덱스는 0부터 시작하므로 +1해줘서 인간의 언어로 만들어주기
