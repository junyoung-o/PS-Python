result_list = [False for _ in range(10001)]

def solution(num):
    if(num > 10000):
        return
    
    result = num
    str_num = str(num)
    digit = len(str_num)

    for i in range(digit):
        result += int(str_num[i])

    if(result < 10001):
        result_list[result] = True

for i in range(10001):
    solution(i)

for i in range(10001):
    if(result_list[i] == False):
        print(i)