#여행가 도착문제

n = input()
sch = input()
direction = {}
count = 0

x, y = (1, 1)

dx = [1, -1]

direction['r'] = dx[0]
direction['l'] = dx[1]
direction['d'] = dx[0]
direction['u'] = dx[1]

for i in sch:
    if i == 'r' or i == 'l':
        y += direction[i]
        print(y)
        if y < 1:
            y = 1

    else:
        x += direction[i]
        print(x)
        if x < 1:
            x = 1

print(x, y)
