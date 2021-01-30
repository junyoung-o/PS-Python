n = int(input())
in_S = input()

m_S = in_S.split(">")
my_S = []
max_n = str()
num = "0123456789"

n_S = in_S.split("<")
ny_S = []
min_n = str()

for i in m_S:
    my_S.append(i.split(" "))

for i in my_S:
    x = i.count("<") + 1
    max_n = max_n + num[-x:]
    num = num[:-x]

print(max_n)

num = "9876543210"

for i in n_S:
    if(">" not in i):
        min_n = min_n + num[-1]
        num = num[:-1]
    else:
        x = i.count(">")
        min_n = min_n + num[-x-1:]
        num = num[:-x-1]
print(min_n)