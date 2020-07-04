def getNthFib(n):
    if n<=0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    nums = [None]*n
    nums[0] = 0
    nums[1] = 1

    for i in range(2,n,1):
        nums[i] = nums[i-1]+nums[i-2]

    return nums[n-1]

def getNthFibBetter(n):
    if n <= 2:
        return n-1
    first = 0
    second = 1
    for n in range(0, n-2):
        current = first + second
        first, second = second, current
    return second

n=10

print(getNthFib(n))

print(getNthFibBetter(n))
    
    
