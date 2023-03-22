# 전화번호부 접두어 문제

# ⓐzip
phone = []


def solution(phone):
    phone.sort()
    for a, b in zip(phone, phone[1:]):
        if b.startswith(a):
            return False
    else:
        True


# ⓑ 해시
hash = {}


def solution2(phone):
    jubdoo = ''
    for i in phone:
        hash[i] = 1
        for j in i:
            jubdoo += j
            if jubdoo in hash and jubdoo != i:
                return False
    return True
