x = [1, 2, 3, 4, 5, 1]

print(x.index(1))




x = [(1, 1),(1, 2),(2, 1)]
x = dict(x)
print(x)


def test():
    global cnt
    for _ in range(100):
        cnt += 1

cnt = 0
for _ in range(100):
    test()

print(cnt)


import time

start = time.time()
x = [i for i in range(100001)]
target = 100000

for i in range(len(x)):
    if(target == x[i]):
        print(True)
        break

finish = time.time()

print("FOR : ", finish - start)


start = time.time()
if(target in x):
    print(True)
finish = time.time()

print("In : ",finish - start)


