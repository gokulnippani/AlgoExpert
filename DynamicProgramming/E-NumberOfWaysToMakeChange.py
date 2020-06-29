def numberOfWaysToMakeChange(n, denoms):
    ways = [0]*(n+1)
    ways[0] = 1

    for denom in denoms:
        for amount in range(denom, len(ways)):
            if amount >= denom:
                ways[amount] += ways[amount-denom]
    return ways[-1]

print(numberOfWaysToMakeChange(6, [1,5]))