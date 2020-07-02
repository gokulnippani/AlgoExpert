def findClosestValueInBst(tree, target):
    # Write your code here.
	if tree is None:
		return None
	expected_result = float("inf")
	while tree is not None:
		if tree.value == target:
			return target
		if abs(target-tree.value) < abs(expected_result-target):
			expected_result = tree.value
		if tree.value<target:
			tree = tree.right
		else:
			tree = tree.left
	return expected_result