import queue

def fibo(n):
    while(n >= 1):
        x = arr.get()
        pre = arr.get()
        arr.put(pre % mod)
        arr.put((x + pre) % mod)
        n -=1

    result = arr.get()

mod = 1000000
p = mod//10 * 15

n = int(input())
n = n % p

arr = queue.Queue()
arr.put(0)
arr.put(1)

print(fibo(n))
