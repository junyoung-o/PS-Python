money = [500,100,50,10,5,1]

cost = int(input())
coin = 0
i = 0

pay_back = 1000 - cost

while(pay_back > 0):
    coin_v = pay_back // money[i]
    pay_back -= coin_v * money[i]
    coin += coin_v
    i += 1

print(coin)