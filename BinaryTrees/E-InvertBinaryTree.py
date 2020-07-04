# Iterative Time o(n), Space O(n)
def invertBinaryTree(tree):
    if tree is None:
		return None
	queue = [tree]
	while len(queue) > 0:
		currentNode = queue.pop()
		if currentNode is None:
			continue
		currentNode.left, currentNode.right = currentNode.right, currentNode.left
        queue.append(currentNode.left)
        queue.append(currentNode.right)
    
    return tree

    # Recursive Time o(n), Space O(d)
def invertBinaryTreeRecursive(tree):
    if tree is None:
		return
	tree.left, tree.right = tree.right, tree.left
    invertBinaryTreeRecursive(tree.left)
    invertBinaryTreeRecursive(tree.right)
    return tree