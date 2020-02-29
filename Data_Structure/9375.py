import sys

get_input = sys.stdin.readline
result = []
testcase = int(get_input())

for _ in range(testcase):
    cloth_set = []
    cloth_sort = {}
    clothes = int(get_input())
    for _ in range(clothes):
        x, y = list(map(str, get_input().split()))

        if(y in cloth_sort):
            cloth_sort[y].append(x)
        else:
            cloth_sort[y] = [x]

    for k, v in cloth_sort.items():
        cloth_set.append(len(v))

    n3 = 1
    for i in cloth_set:
        n3 *= (i+1)
    result.append(n3-1)

for i in result:
    print(i)