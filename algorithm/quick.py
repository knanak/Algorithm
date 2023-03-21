# 퀵정렬 구현 : pivot을 기준으로 앞 뒤를 쪼개면서 정렬, 재귀적
arr = [5, 4, 3, 8, 0, 1, 2]


def quick1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]  ## pivot보다 작으면 왼쪽으로 정렬
    right = [x for x in tail if x > pivot]

    return quick1(left) + [pivot] + quick1(right)


def quick2(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        while (right >= start and arr[right] <= arr[pivot]):
            right -= 1

        if (right < left):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick2(arr, start, right - 1)
    quick2(arr, right + 1, end)


quick2(arr, 0, len(arr) - 1)
