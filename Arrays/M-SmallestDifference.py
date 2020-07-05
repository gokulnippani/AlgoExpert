def smallestDifference(arrayOne, arrayTwo):
    i = 0
    j = 0
    difference = float("inf")
    pair = None
    while i<len(arrayOne) and j<len(arrayTwo):
        if arrayOne[i] == arrayTwo[j]:
            return [arrayOne[i], arrayOne[i]]
        current_diff = abs(arrayOne[i] - arrayTwo[j])
        if current_diff < difference:
            difference = current_diff
            pair = [arrayOne[i],arrayTwo[j],]
        if arrayTwo[j]<arrayOne[i]:
            j += 1
        else:
            i += 1
    return  pair

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))