def hanoi(num, start, end, helper):
    if num == 0:
        return
    if num == 1:
        print(start, "->", end)

    hanoi(num - 1, start, helper, end)
    print(start, "->", end)
    hanoi(num - 1, helper, end, start)


num = int(input("원판의 갯수는?"))
hanoi(num, "start", "helper", "end")
