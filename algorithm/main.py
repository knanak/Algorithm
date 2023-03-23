## 정렬 알고리즘 구현하기
list = [5, 7, 3, 1, 2, 9, 0]

#### o(n^2) : 버블, 선택, 삽입정렬
# a. 버블 정렬 : 옆에 있는 데이터와 비교하여 작은 값을 앞으로 보냄. 정렬이 끝날때마다 가장 큰 값이 맨 뒤로 가는 효과가 발생함
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)

# b. 선택정렬 : 가장 작은 값을 선택해서 맨 앞 데이터와 바꾸는 것을 반복
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)

# c. 삽입정렬 : 현재 데이터를 왼쪽값과 비교하여 적절한 위치에 삽입. 적절한 위치라고 판단될 경우에만 스왑이 일어나기 때문에 o(n^2)중에서는 가장 빠르다. 정렬이 될떄마다 왼쪽에 있는 데이터는 이미 정렬된 것으로 간주한다.
for i in range(1, len(list)):
    min = i
    for j in range(i, 0, -1):
        if list[i] < list[j]:
            min = j
            list[i], list[min] = list[min], list[i]
print(list)


#### o(n logn) : 분할상환(퀵, 머지)
# d. 퀵정렬 : pivot값을 기준으로 왼쪽은 작은값, 오른쪽은 큰값으로 분할하여 재귀적으로 정렬을 수행. pivot값이 한쪽으로 쏠릴경우 선형탐색의 구조가 나오기 때문에 o(n^2)으로 증가함
def quick(arr):
    if len(arr) <= 1:  ## 재귀함수의 종료조건
        return arr

    pivot = arr[0]
    tail = arr[1:]

    right = [x for x in tail if x >= pivot]
    left = [x for x in tail if x < pivot]

    # right = []
    # left = []
    # for i in tail:
    #     if pivot <= i:
    #         right.append(i)
    #     else:
    #         left.append(i)

    return quick(left) + [pivot] + quick(right)

quick(list)

def quick2()