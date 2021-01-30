def fibo(n):
    n1 = 0
    n2 = 1
    while(n > 1):
        list.append((list[n1] + list[n2]) % mod)
        n1 += 1
        n2 += 1
        n -= 1
    result = list[-1]
    return result

mod = 1000000
p = mod//10 * 15

n = int(input())
n = n % p

list = [0, 1]
print(fibo(n))
