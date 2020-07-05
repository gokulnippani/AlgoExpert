def maxSumIncreasingSubsequence(array):
    # Write your code here.
	sums = array[:]
	sequence = [None]*len(array)
	CalculateMaxSum(array,sums,sequence)
	idx = GetMaxSumIndex(sums)
	max_sequence = GetMaxSequence(sequence, idx,array)
	return [sums[idx],max_sequence]

def CalculateMaxSum(array,sums,sequence):
	for i in range(0,len(array)):
		current_element = array[i]
		for j in range(0,i):
			other_element = array[j]
			if current_element > other_element:
				current_sum = current_element+sums[j]
				if current_sum > sums[i]:
					sums[i] = current_sum
					sequence[i] = j
					
def GetMaxSumIndex(sums):
	max_idx = 0
	for i in range(1, len(sums)):
		if sums[i] > sums[max_idx]:
			max_idx = i
	return max_idx

def GetMaxSequence(sequence, idx,array):
	max_seq = []
	while idx is not None:
		max_seq = [array[idx]]+max_seq
		idx = sequence[idx]
	return max_seq

print(maxSumIncreasingSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

a = [3]
a.extend([2])
print(a)
		
		
					
	
	
