
# Coding Change Problem (version 3?)

## Statement

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, ... , Sm} valued coins, found the number of coins of each denomination that results in the minimal number of coins used. 

## Solution

The only solution I seemed to find was to use a variation of the classic Knapsack Problem with infinite supply elements.

The very first thing to notice is that the Knapsack problem solution provides insite of the minimal number of coins to be used, but not the number for each coin. In order to do so we may use a matrix of NxM (where, as mentioned in the statement, N is the number of cents we need to provide, and M is the number of coins we have). Each file of this matrix, then represents the number of coins involved in the optimal solution. 

So, given this setup, we just need to add some extra caviets in order to make it work. This is a sample nicely formulated code in python of the Knapsack problem.

```python
import math 
def ks(n,coins):

  """
    n: int n cents to be given as change
    coins: list of coins 
    min_coins: array that contains the minimum 
    number of coins for each value of change
    
  
  """
  min_coins = [0 for x in range(n+1)]
  for nn in range(1,n+1):
    min_coins[nn] = math.inf
    for c in coins:
      if nn >= c:
        num_coins = min_coins[nn-c] + 1
        if num_coins < min_coins[nn-c]:
          min_coins[nn-c] = num_coins
  
  return min_coins[n]

```

Now to extrapolate this problem to higher dimentions we need to change that "+1" at the end of line 33 and convert it into 
a column matrix that is able to be sum (element by element) with the column of the "nn-c" index of min_coins. We may do this by using the python map function like the code below.

```python
indent = {}
for i in range(len(coins)):
  ident[coins[i]] = [ 0 if x != i else 1 for x in range(len(coins))]
```
This gives of a dictionary that maps each coin denomination into a column matrix with only 1 at each corresponding position. The next thing is to sum column matrices (without the help of numpy of course). This is done below easily: 

```python
def matrix_sum(a1, a2):
    return list(map(lambda x,y: x + y, a1,a2))
``` 

Another thing we need is how we are going to compare the variable num to the column of min_coins. In order to do so, we use the sum() function of python to some all the content of the array and compare the minimum number of coins stored in both arrays. That's it we have all we need, now to wrap it all up below is the entire code that prints in the following format {
coin1: val1, coin2: val2, ... coinN: valN}.

```python
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

```
