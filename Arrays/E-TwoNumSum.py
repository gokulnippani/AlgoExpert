def twoNumberSum(array, targetSum):
    # Write your code here.
	a=set()
	for i in array:
		if targetSum-i in a:
			if i> targetSum-i:
			    return [targetSum-i,i]
			return [i,targetSum-i]
		else:
			a.add(i)
	return []

print(twoNumberSum([-7,-5,-3,0,1,4],-3))