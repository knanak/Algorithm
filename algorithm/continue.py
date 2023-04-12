# 캐릭터의 좌표
keyinput = ["down", "down", "down", "down", "down"]
board = [7, 9]

## 답 : [0, -4]


# 1. 비교문, 부등호로 board의 범위 설정
def solution(keyinput, board):
    x, y = 0, 0
    for i in keyinput:
        if -(board[1] // 2) < y < board[1] // 2:
            if i == 'up':
                y += 1

            elif i == 'down':
                y -= 1

        if -(board[0] // 2) < x < board[0] // 2:
            if x == 'right':
                x += 1

            elif i == 'left':
                x -= 1

    return [x, y]


print(solution(keyinput, board))


# 2. max(), min()으로 범위 제한
def solution2(keyinput, board):
    x, y = 0, 0
    for i in keyinput:
        if i == 'up':
            y = min(y + 1, board[1] // 2)

        elif i == 'down':
            y = max(y - 1, -(board[1] // 2))

        elif i == 'right':
            x = min(x + 1, board[0] // 2)

        elif i == 'left':
            x = max(x - 1, -(board[0] // 2))

    return [x, y]


print(solution2(keyinput, board))


# 3. dict
def solution3(keyinput, board):
    dict = {'up': [0, 1], 'down': [0, -1], 'right': [1, 0], 'left': [-1, 0]}
    x, y = 0, 0

    for i in keyinput:
        dx, dy = dict[i]
        if abs(x + dx) > board[0] // 2 or abs(y + dy) > board[1] // 2:
            continue
        else:
            x, y = dx + x, dy + y
    return [x, y]


print(solution3(keyinput, board))
