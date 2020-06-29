def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]
	max_sum_2 = array[0]
	max_sum_1 = max(array[1],array[0])
	for i in range(2,len(array)):
		current_max = max(array[i]+max_sum_2, max_sum_1)
		max_sum_2 = max_sum_1
		max_sum_1 = current_max
	return max(max_sum_1, max_sum_2)

array = [75, 105, 120, 75, 90, 135]

print(maxSubsetSumNoAdjacent(array))