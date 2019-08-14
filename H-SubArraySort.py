# Solution 1 : Time Complexity is O(nlogn) and space complexity is O(n)
# Solution 2 : Time Complexity is O(n) and space complexity is O(1)
def subarraySort(array):
    # Find the start and end of unsorted array
    result = [-1,-1]
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            result[0] = i-1
            result[1] = len(array)-1
            break
    if result[0] == -1:
        return result
    for j in range(len(array)-2,-1,-1):
        if array[j] > array[j+1]:
            result[1] = j+1
            break
    min = array[result[0]]
    max = array[result[1]]
    for i in range(result[0],result[1]+1,1):
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]
    for i in range(0,result[0]):
        if array[i] > min:
            result[0] = i
            break
    for j in range(result[1] + 1,len(array),1):
        if array[j] < max:
            result[1] = j
        else:
            break
    return result



print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))

print(subarraySort([1, 2, 8, 4, 5]))