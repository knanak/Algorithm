# 정렬 알고리즘
#1) 선택정렬 : o(n^2)- 이중반복문을 사용하는 경우

list = [1, 5, 3, 2, 0, 9, 7, 6]

# ⓐlist2.append()
list2 = []

for i in range(len(list)):  # in list가 안되는 이유
    list2.append(min(list))
    list.remove(min(list))
print(list2)

#ⓑ이중반복문
for i in range(len(list)):
    current = i
    for j in range(current + 1, len(list)):
        if list[current] > list[j]:
            current = j
    list[i], list[current] = list[current], list[i]

print(list)

#ⓒmin이용
for i in range(len(list)):
    listE = list[i:]
    m = min(listE)
    m = list.index(
        m)  #listE.index(m)의 경우, 인덱스가 변동됨. 고정된 기준인 index를 위해 수정되지 않은 list를 사용
    list[i], list[m] = list[m], list[i]

print(list)

# 2) 삽입정렬
for i in range(1, len(list)):
    for j in range(i, 0, -1):
        if list[j] < list[j - 1]:
            list[j], list[j - 1] = list[j - 1], list[j]
        else:
            break

print(list)

