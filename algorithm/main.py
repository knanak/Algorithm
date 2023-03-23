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


def quick2(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while (arr[pivot] >= arr[left] and left <= end):
            left += 1

        # right는 pivot과 같을 수 없기 때문에 right != start
        while (arr[pivot] <= arr[right] and right > start):
            right -= 1

        if (left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick2(arr, start, right - 1)
    quick2(arr, right + 1, end)


quick2(list, 0, len(list) - 1)  ## -1이 없으면 69번째에서 list index out of range
print(list)

# e. 머지정렬 : 정렬되지 않은 배열을 하나의 데이터가 남을때까지 분할한 뒤에 합치면서 정렬한다. 즉, n개의 데이터를 /2 하여 하나의 데이터가 남을 때까지 재귀적으로 나누고, 이를 왼쪽과 오른쪽으로 구분해 새로운 리스트에 담는다. 왼쪽과 오른쪽의 데이터를 병합하며 정렬한다. 별도의 pivot값을 설정할 필요없이 배열의 중간위치의 값을 기준으로 나누고 합치기 때문에 항상 o(n logn)의 시간복잡도를 보장한다. 하지만 정렬한 값을 저장할 추가적인 배열이 필요하기에 메모리가 없거나, 메모리 효율을 추구할 경우에는 바람직하지 않다.


def divide(arr):
    if len(arr) <= 1:
        return arr  ## 재귀의 종료 조건은 맨처음에 와야 무한반복을 값을 거를 수 있다.

    mid = len(arr) // 2
    left = arr[mid:]
    right = arr[:mid]

    return merge(divide(left), divide(right))


def merge(left, right):
    i = 0
    j = 0
    sorted = []

    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    while i < len(left):
        sorted.append(left[i])
        i += 1

    while j < len(right):
        sorted.append(right[j])
        j += 1

    return sorted


print(divide(list))
