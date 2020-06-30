def fourNumberSum(array, targetSum):
    array.sort()
    print(array)
    i=0
    pairs = {}
    result = []
    while(i < len(array)-1):
        primary_ele = array[i]
        j= i+1
        while(j < len(array)):
            current_sum = primary_ele + array[j]
            if targetSum - current_sum in pairs:
                for pair in pairs[targetSum - current_sum]:
                    current_pair = [primary_ele , array[j]]
                    current_pair.extend(pair)
                    result.append(current_pair)
            j += 1
        j = i
        primary_ele = array[j]

        # We add the pair after we visited the elements after the element to aviod dups
        while j>0:
            j -= 1
            current_ele = array[j]
            current_sum = current_ele+primary_ele
            current_pair = [current_ele,primary_ele]
            if current_sum not in pairs:
                pairs[current_sum] = [current_pair]
            else:
                pairs[current_sum].append(current_pair)
        i += 1

    return result

print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))