# 로그인 성공?
id_pw = ["rabbit04", "98761"]
db = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]


# 1. 비교문
def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'


print(solution(id_pw, db))


# 2. dict
def solution2(id_pw, db):
    db = dict(db)
    if db.get(id_pw[0]):
        if db.get(id_pw[0]) == id_pw[1]:
            return 'login'
        else:
            return 'wrong pw'
    return 'fail'


print(solution2(id_pw, db))
