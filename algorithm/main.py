# a를 정렬해서 b로 만들수 있는가

b = "allpe"
a = "apple"


# 1. sorted()
def solution(b, a):
    return 1 if sorted(b) == sorted(a) else 0


print(solution(b, a))


#2. str.replace('-를', '-로', 몇번 변경)
def solution2(b, a):
    for i in b:
        if i in a:
            a = a.replace(i, '', 1)
            if len(a) == 0:
                return 1
    return 0


print(solution2(b, a))
