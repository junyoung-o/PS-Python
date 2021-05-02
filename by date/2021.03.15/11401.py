import time
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
div = 1000000007

def is_over(num):
    if(num >= div):
        return True
    return False

def get_div(num):
    return num % div

def get_process(num1, num2):
    if(is_over(num1)):
        num1 = get_div(num1)
    return num1 * num2

def get_result():
    up = n
    bottom = k
    for i in range(1, k):
        up = get_process(up, up-i)
        bottom = get_process(bottom, bottom-i)

    result = up//bottom
    if(is_over(result)):
        return get_div(result)

    return get_div(result)

s = time.time()
print(get_result())
print(time.time() - s)