# 잔돈으로 500,100,50,10,5,1
# 거스름돈 가장 적게 잔돈을 준다
# 천엔 냈을 때 잔돈에 포함된 잔돈의 개수

price = int(input())

change = 1000 - price
coins = [500, 100, 50, 10, 5, 1]
i = 0
coin_count = 0
while i != 6:
    if change // coins[i]:
        coin_count += change // coins[i]
        change = change - coins[i] * (change // coins[i])
        i += 1
    else:
        i += 1
        
print(coin_count)