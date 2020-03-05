import math 
cash = int(input())
coins = list(map(lambda x: int(x), str(input()).strip().split()))

def matrix_sum(a1, a2):
    return list(map(lambda x,y: x + y, a1,a2))

def change(cash):
    
    ident = {}
    for i in range(len(coins)):
        ident[coins[i]] = [ 0 if x != i else 1 for x in range(len(coins))]

    min_coins = [[0 for x in range(len(coins))] for i in range(cash+1)]
    for m in range(1,cash+1):
        min_coins[m] = [math.inf, math.inf, math.inf]
        for c in coins:
            if m >= c:
                num = matrix_sum(min_coins[m-c],ident[c])
                if sum(num) < sum(min_coins[m]):
                    min_coins[m] = num

    print(dict(map(lambda x,y: (x,y),coins, min_coins[cash])))

change(cash)


