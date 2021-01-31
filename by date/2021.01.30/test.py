import time

test_list = [i for i in range(100000000)]
result = []

start = time.time()
for i in test_list:
    if(i<10):
        result.append(i)

finish = time.time()

print("For : ", finish - start)

start = time.time()

result = list(filter(lambda a : a < 10, test_list))

finish = time.time()

print("filter : ", finish - start)
