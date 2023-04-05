# 7의 갯수 : list를 str으로 변경해서 count()하기
arr = [7, 77, 17]


# 1. 이중 반복문 : for in
def solution(arr):
    chr = []
    for i in arr:
        chr.append(str(i))

    result = 0
    for i in chr:
        for j in i:
            if j == '7':
                result += 1
    return result


print(solution(arr))


# 2. list/str.count(값)
def solution2(arr):
    chr = ''
    for i in arr:
        chr += str(i)
    return chr.count('7')


print(solution2(arr))


## list를 string으로 변경하는 방법
## 1. ''.join(list)
def solution3(arr):
    return ''.join(map(str, arr)).count('7')


print(solution3(arr))


## 2. str(list)
def solution4(arr):
    return str(arr).count('7')


print(solution4(arr))


## 3. 반복문
def solution5(arr):
    return sum([str(i).count('7') for i in arr])


print(solution5(arr))
