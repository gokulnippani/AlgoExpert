def validateBst(tree):
    # Write your code here.
    return ValidatBstHepler(tree, float("inf"), float("-inf"))


def ValidatBstHepler(tree, max, min):
    if not tree:
        return True
    if tree.value <= min or tree.value > max:
        return False
    leftValid = ValidatBstHepler(tree.left, tree.value, min)
    return leftValid and ValidatBstHepler(tree.left, max, tree.value)
