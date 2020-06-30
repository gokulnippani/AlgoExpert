def levenshteinDistance(str1, str2):
    # Write your code here.
	if len(str1)==0 and len(str2)==0:
		return 0
	if len(str1) == 0:
		return len(str2)
	if len(str2) == 0:
		return len(str1)
	distance = [[i for i in range(len(str1)+1)] for i in range(len(str2)+1)]
	
	for i in range(1,len(str2)+1):
		for j in range(len(str1)+1):
			
			if str2[i-1] == str1[j-1]:
				distance[i][j] = distance[i-1][j-1]
			else:
				distance[i][j] = 1+ min(distance[i][j-1],distance[i-1][j],distance[i-1][j-1])
	return distance[-1][-1]
				
print(levenshteinDistance("abc","yadb"))

