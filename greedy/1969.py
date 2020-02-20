N, M = list(map(int, input().split()))
DNA = []
result = str()
r = 0

for _ in range(N):
    DNA.append(str(input()))

my_n = [["A", 0], ["T", 0], ["G",0], ["C",0]]
for i in range(M):
    for x in DNA:
        for n in range(4):
            if(x[i] == my_n[n][0]):
                my_n[n][1] += 1
        my_n.sort(key = lambda x: x[0]) 
        my_n.sort(key = lambda x : x[1], reverse = True)
    result += my_n[0][0]
    my_n = [["A", 0], ["T", 0], ["G",0], ["C",0]]

for i in range(M):
    for x in DNA:
        if(x[i] != result[i]):
            r+= 1

print(result)
print(r)