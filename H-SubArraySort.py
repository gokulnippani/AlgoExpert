# Time Complexity is O(nlogn) and space complexity is O(n)
def subarraySort(array):
    sorted_array = array[:]
    sorted_array.sort()

    result = [-1,-1]

    for i in range(len(array)):
        if array[i] != sorted_array[i]:
            result[0] = i
            result[1] = len(array)-1
            break

    if result[0] == -1:
        return result

    j = len(array) - 1

    while(j>i):
        if array[j] != sorted_array[j]:
            result[1] = j
            break
        j-=1

    return result

print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))