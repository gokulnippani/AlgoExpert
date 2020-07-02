# Solution 1 is recursively. Because we have call stack
# Solution 2 is iterative.
def binarySearch(array, target):
    if not array:
        return -1
    return binarySearchHelper(0, len(array)-1, array, target)


def binarySearchHelper(low, high, array, target):
    while low <= high:
        mid = (high - low) // 2 + low
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
