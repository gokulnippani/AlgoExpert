# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
# The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with
#     respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.

def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(0, len(array)-2):
        current_element = array[i]
        print(current_element)
        pointer_1 = i+1
        pointer_2 = len(array)-1
        while(pointer_1<pointer_2):
            current_sum = current_element+array[pointer_1]+array[pointer_2]
            if current_sum == targetSum:
                result.append([current_element, array[pointer_1], array[pointer_2]])
                pointer_2 -= 1
                pointer_1 += 1
            elif current_sum<targetSum:
                pointer_1 += 1
            else:
                pointer_2 -= 1

    return result


print(threeNumberSum([-10,100,-50,7,10,99,290,0,-1,-3,-11],-21))