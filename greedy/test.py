def hanoi(disk, start, mid, end):
    if disk == 1:
        print("start : {}, mid : {}, end : {}".format(start, mid, end))
    else:
        # print("start : {}, min : {}, end : {}".format(start, mid, end))
        hanoi(disk - 1, start, end, mid)
        print("start : {}, mid : {}, end : {}".format(start,mid, end))
        hanoi(disk - 1, mid, start, end)

total_disk = int(input())
total_mvmt = 0

for disk in range(total_disk):
    total_mvmt = total_mvmt * 2
    total_mvmt += 1

print(total_mvmt)
hanoi(total_disk, 1, 2, 3)