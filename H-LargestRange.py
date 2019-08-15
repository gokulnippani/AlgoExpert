# Solution 1 Time Complexity is O(n log n) - For sort
# Sort the array and run for loop. Compare current element with previous. If equal continue else if greater than one increment current range by 1
# Make sure to compare range after loop ends
def largestRange(array):
    if len(array) < 1:
        return None
    array.sort()
    largestRange = 1
    currentRange = 1
    largestElemts = [array[0], array[0]]
    for i in range(1, len(array), 1):
        if array[i] == array[i - 1]:
            continue
        if array[i] == array[i - 1] + 1:
            currentRange += 1
            continue
        else:
            if currentRange > largestRange:
                # Build potential result
                largestElemts = [array[i] - currentRange + 1, array[i - 1]]
                largestRange = currentRange
            currentRange = 1

    if currentRange > largestRange:
        # Build potential result
        largestElemts = [array[len(array) - 1] - currentRange + 1, array[len(array) - 1]]
    return largestElemts


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))

print(largestRange(
    [0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]))

print(largestRange(
    [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6,
     13, 14, -4, -2]))
