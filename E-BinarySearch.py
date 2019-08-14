def binarySearch(array, target):
    if not array:
        return -1
    return binarySearchHelper(0, len(array), array, target)


def binarySearchHelper(low, high, array, target):
    if low > high:
        return -1
    # Type conversion. Change float to int.
    mid = int((low + high) / 2)
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binarySearchHelper(mid + 1, high, array, target)
    else:
        return binarySearchHelper(low, mid - 1, array, target)


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
