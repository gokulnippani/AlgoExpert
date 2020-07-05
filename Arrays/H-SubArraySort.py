# Solution 1 : Time Complexity is O(nlogn) and space complexity is O(n). It's naive approch
# Solution 2 : Time Complexity is O(n) and space complexity is O(1). Below solution. View History for another version.
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        if IsOutOfOrder(i, array):
            minOutOfOrder = min(array[i], minOutOfOrder)
            maxOutOfOrder = max(array[i], maxOutOfOrder)
    
    if minOutOfOrder == float("inf"):
        return [-1,-1]
    
    subarrayLeftIdx, subarrayRightIdx = 0, len(array)-1

    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx+=1
    
    while maxOutOfOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -=1

    return [subarrayLeftIdx, subarrayRightIdx]

def IsOutOfOrder(i, array):
    num = array[i]
    if i==0:
        return num > array[i+1]
    
    if i == len(array)-1:
        return num < array[i-1]
    
    return num > array[i+1] or num < array[i-1]


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))

print(subarraySort([1, 2, 8, 4, 5]))