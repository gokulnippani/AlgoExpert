def longestCommonSubsequence(str1, str2):
    # Write your code here.
	if len(str1) ==0 or len(str2) == 1:
		return []
	array = [[0 for x in range(len(str2)+1)] for x in range(len(str1)+1)]
	#array = [[0]* (len(str2)+1)] *(len(str1)+1)
	#array = [[0]*range(len(str2)+1) for i in range(len(str1)+1)]
	for row in range(1,len(str1)+1):
		for column in range(1,len(str2)+1):
			if str1[row-1] == str2[column-1]:
				array[row][column] = array[row-1][column-1]+1
			else:
				array[row][column] = max(array[row-1][column],array[row][column-1])
	row = len(str1)
	column = len(str2)
	result = []
	while row!=0 and column !=0:
		if array[row][column] == array[row][column-1]:
			column -= 1
		elif array[row][column] == array[row-1][column]:
			row -= 1
		else:
			result.append(str1[row-1])
			row -= 1
			column -= 1
	return list(reversed(result))