def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float("inf") for _ in range(n+1)]
    numOfCoins[0] = 0

    for denom in denoms:
        if denom<=n:
            for amount in range(len(numOfCoins)):
                numOfCoins[amount] = min(numOfCoins[amount], 1+numOfCoins[amount-denom])
    
    return numOfCoins[-1] if  numOfCoins[-1] != float("inf") else -1

print(minNumberOfCoinsForChange(7, [1,5,10]))